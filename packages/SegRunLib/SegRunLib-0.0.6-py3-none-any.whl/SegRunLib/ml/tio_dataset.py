import os
import numpy as np
import nibabel as nib
import pandas as pd
import torch
import torchio as tio
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import torch.nn as nn
import torch.nn.functional as F


class TioDataset(Dataset):
    def __init__(self, data_dir,
                 train_settings=None,
                 val_settings=None,
                 test_settings=None):
        
        super(Dataset, self).__init__()
        self.data_dir = data_dir
        self.train_settings = train_settings
        self.val_settings = val_settings
        self.test_settings = test_settings
        
        self.train_data = None
        self.val_data = None
        self.test_data = None
        
        self.train_dataloader = None
        self.val_dataloader = None
        self.test_dataloader = None
        
        if train_settings is not None:
            self.train_data = self.set_data(data_type='train')
            self.train_dataloader = self.set_dataloader(data_type='train')
            
        if val_settings is not None:
            self.val_data = self.set_data(data_type='val')
            self.val_dataloader = self.set_dataloader(data_type='val')
            
        if test_settings is not None:
            self.test_data = self.set_data(data_type='test')
            self.test_dataloader = self.set_dataloader(data_type='test')
            
        
    def set_data(self, data_type):
        if data_type=='train':
            path_to_data = self.data_dir + "/train"
        elif data_type=='val':
            path_to_data = self.data_dir + "/val"
        elif data_type=='test':
            path_to_data = self.data_dir + "/test"
        else:
            raise RuntimeError("HeadDataset::set_data ERROR")

        subjects_list = []
        for dirname, dirnames, filenames in os.walk(path_to_data):
            for subdirname in dirnames:
                p = os.path.join(dirname, subdirname)
                subject_dict = {'head': tio.ScalarImage(p + '/head.nii.gz'),
                                'vessels': tio.LabelMap(p + '/vessels.nii.gz'),
                                "sample_name" : subdirname}
                subject = tio.Subject(subject_dict)
                if data_type=='train' and self.train_settings["sampler"]=="weighted":
                    self.add_prob_map(subject)
                subjects_list.append(subject)      
        return(tio.SubjectsDataset(subjects_list))


    def add_prob_map(self, subject, focus=1.5):
        _, h, w, d = subject.shape
        x0 = h//2
        y0 = w//2
        prob_slice = np.ones((h,w))

        for x in range(prob_slice.shape[0]):
            for y in range(prob_slice.shape[1]):
                prob_slice[x, y] = ((focus-((x/x0-1)**2 + (y/y0-1)**2)**0.5))

        prob_slice = prob_slice.clip(0, 1)
        prob_vol = np.stack(d*[prob_slice,], axis=2)

        prob_Image = tio.Image(tensor=torch.tensor(prob_vol).unsqueeze(0),
                               type=tio.SAMPLING_MAP,
                               affine=subject.head.affine)
        subject.add_image(prob_Image, "prob_map")
        return(subject)
    
    
    def set_dataloader(self, data_type):
        if data_type=='train':
            settings = self.train_settings
            data = self.train_data
        elif data_type=='val':
            settings = self.val_settings
            data = self.val_data
        elif data_type=='test':
            settings = self.test_settings
            data = self.test_data
        else:
            raise RuntimeError("HeadDataset::set_data ERROR")    
        
        
        if data_type in ('train', 'val'): 
            if settings["sampler"] == "weighted":
                sampler = tio.data.WeightedSampler(settings["patch_shape"],
                                                   probability_map='prob_map')
            else:
                sampler = tio.data.UniformSampler(settings["patch_shape"])
            
            patches_queue = tio.Queue(
                data,
                settings["patches_queue_length"],
                settings["patches_per_volume"],
                sampler,
                num_workers=settings["num_workers"],
            )

            patches_loader = DataLoader(
                patches_queue,
                batch_size=settings["batch_size"],
                num_workers=0,  #must be
            )
            return(patches_loader)
        else: #data_type='test'
            return(torch.utils.data.DataLoader(data, batch_size=1, shuffle=False))
            # test_loaders = []
            # for subject in data:
            #     grid_sampler = tio.GridSampler(subject,
            #                                    patch_size=settings["patch_shape"],
            #                                    patch_overlap=settings["overlap_shape"])
            #     grid_aggregator = tio.data.GridAggregator(sampler=grid_sampler, overlap_mode='hann')
            #     patch_loader = torch.utils.data.DataLoader(grid_sampler,
            #                                                batch_size=settings["batch_size"],
            #                                                num_workers=settings["num_workers"])
            #     GT = subject.vessels
            #     sample_name = subject.sample_name
            #     test_loaders.append({"patch_loader" : patch_loader,
            #                          "grid_aggregator" : grid_aggregator,
            #                          "GT" : GT,
            #                          "sample_name" : sample_name})
            # return(test_loaders)
        
        