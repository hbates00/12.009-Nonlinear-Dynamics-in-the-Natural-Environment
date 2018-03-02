# -*- coding: utf-8 -*-
"""
Created on Tue May 16 20:05:07 2017

@author: Haley
"""

import numpy as np
import scipy
import matplotlib.pyplot as plt

matdata = scipy.io.loadmat('vostok.mat')
g = matdata['OxygenIsotopesd18O'][0]
data = np.array(g)


var_set = np.var(data)
std_set = np.std(data)
mean_set = np.mean(data)
num_samples = len(data)

data = data[:] - mean_set
transform = np.fft.rfft(data)
transform = np.abs(transform)**2

f = np.linspace(0, .5, np.size(transform))

def w_noise_floor():
    array = np.zeros((208, 100))
    
    for i in range(99):
        x = np.random.normal(mean_set, std_set, size=num_samples)
        mean = np.mean(x)
        
        x = x - mean
        transx = np.fft.rfft(x)
        transx = np.abs(transx)**2
        
        for j in range(len(transx)-1):
            array[j][i] = transx[j]
    
    return array
    
def r_noise_floor():
    array = np.zeros((208, 100))
    
    for i in range(99):
        r = [0]*num_samples
        dt = [-1, 1]
    
        for k in range(1, num_samples):
            r[k] = r[k-1] + np.random.choice(dt)
        
        r = np.array(r)   
        var_red = np.var(r)
        
        factor = var_set/var_red
        r = r*np.sqrt(factor)
        
        r = r - np.mean(r)
        
        transx = np.fft.rfft(r)
        transx = np.abs(transx)**2
        
        for j in range(len(transx) -1):
            array[j][i] = transx[j]
            
    return array

    
def sort_floor(array):
    x = np.array(array, copy = True)
    
    for i in range(len(x)):
        l = x[i][:]
        l.sort()
        x[i] = l
    
    return x

def get_floor(array):
    x = array[:]
    floor = []
    
    for i in range(len(x)):
        floor.append(x[i][94])
        
    return floor
            
red_floor = r_noise_floor()
red_floor = sort_floor(red_floor)
red_floor = get_floor(red_floor)

white_floor = w_noise_floor()
white_floor = sort_floor(white_floor)
white_floor = get_floor(white_floor)

#plt.plot(f, transform, color = 'k', label = 'Oxygen Isotope d18O Data')
#plt.plot(f, white_floor, color = 'b', label = 'White Noise FLoor')
plt.plot(f, red_floor, color ='r', label = 'Red Noise Floor')

'''
plt.axvline(x = .01, label = 'Combined Eccentricity Frequency', color= '#ef1010', linestyle='--')
plt.axvline(x = .0388, label = 'Axial Precession Frequency', color='#ff6600', linestyle='--')
plt.axvline(x = .008928, label = 'Apsidal Precession Frequency', color='#6708db', linestyle='--')
plt.axvline(x = .014285, label = 'Orbital Inclination Frequency', color='#b700b7', linestyle='--')
'''
plt.title('Period Power of Oxygen Isotope d18O Data Compared to Colored Noise Floors')
plt.xlabel('Frequency 1/1000yrs')
plt.ylabel('Power')
plt.legend()
plt.xscale('log')
plt.yscale('log')

plt.xlim(0, .45)
plt.ylim(1, 7000)
