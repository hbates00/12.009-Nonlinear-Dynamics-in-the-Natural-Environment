# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 02:22:21 2017

@author: Haley
"""

import scipy
import matplotlib.pyplot as plt
import numpy as np

matdata = scipy.io.loadmat("Fracture.mat")
data_raw = matdata['Fracture']

def get_const_points(data):
    
    const = (data == 1)
    return const
    
def build_usable_data(data):
    
    new = np.copy(data)  
    
    for i in range(len(data)):
        for j in range(len(data)):
            if i == (len(data) - 1):
                new[i][j] = 1
            elif data[i][j] == 1:
                new[i][j] = 0
            else:
                new[i][j] = 1
    
    new = new.astype(np.float32)
    return new

def average(data, const):
    
    dat = np.copy(data)
    for i in xrange(1, data.shape[0] - 1):
        
        j = 0
        av = ((data[i + 1][j] + data[i - 1][j] + data[i][j + 1])/3.0)
        dat[i][j] = av
        
        j = len(data) -1
        
        av = ((data[i + 1][j] + data[i - 1][j] + data[i][j - 1])/3.0)
        dat[i][j] = av
            
    dat[1:-1, 1:-1] = (data[2:, 1:-1] + data[:-2, 1:-1] + data[1:-1, 2:] + data[1:-1, :-2])/4.0
    dat[const] = 0
    dat[0, :] = 0
    dat[-1, :] = 1
    return dat
    

def loop_average(data, t):
    
    const_points = get_const_points(data)
    data = build_usable_data(data)
    dat = np.copy(data)
    
    for k in range(t):
        m = average(dat, const_points)
        dat = m
        
    return dat
    
def find_flux_profile(data):
    dat = np.copy(data)
    
    for i in xrange(1, data.shape[0] - 1):
        j = 0
        flux = np.sqrt((data[i + 1][j] - data[i - 1][j])**2 + (data[i][j + 1])**2)
        dat[i, j] = flux
        
        j = len(data) - 1
        flux = np.sqrt((data[i + 1][j] - data[i - 1][j])**2 + (data[i][j - 1])**2)
        dat[i, j] = flux
    
    dat[1:-1, 1:-1] = ((data[2:, 1:-1] - data[:-2, 1:-1])**2 + (data[1:-1, 2:] - data[1:-1, :-2])**2)
    
    return dat
    
processed_data = loop_average(data_raw, 30000)
flux = find_flux_profile(processed_data)

    
plt.imshow(flux, cmap='hot', interpolation='nearest')
plt.colorbar(cmap = 'hot')
plt.xlabel('X Position')
plt.ylabel('Z Position')
plt.title('Magnitude of Flux for Fractured Seafloor Slab')
plt.show()
