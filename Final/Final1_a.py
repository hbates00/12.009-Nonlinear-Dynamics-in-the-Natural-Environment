# -*- coding: utf-8 -*-
"""
Created on Mon May 15 17:19:05 2017

@author: Haley
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy


matdata = scipy.io.loadmat('vostok.mat')
g = np.array(matdata['OxygenIsotopesd18O'][0])
x = np.arange(0, 414)

var_set = np.var(g)
std_set = np.std(g)
mean_set = np.mean(g)
num_samples = len(g)

#------------- white noise -------------

w = np.random.normal(mean_set, std_set, size=num_samples)
mean_w = np.mean(w)
var_w = np.var(w)

#------------- red noise -------------

r = [0]*num_samples
dt = [-1, 1]

for i in range(1, num_samples):
    r[i] = r[i-1] + np.random.choice(dt)

r = np.array(r)   
var_red = np.var(r)
std_red = np.std(r)
mean_red = np.mean(r)

factor = var_set/var_red
r = r*np.sqrt(factor)

diff = mean_set - np.mean(r)
r = r + diff

mean_r = np.mean(r)
var_r = np.var(r)

#------------- plotting -------------

plt.plot(x, g, label = 'Oxygen Isotope delta-18O Dataset (Mean = %s, Variance = %s)' % (round(mean_set,2), round(var_set, 2)), color = 'k')
plt.plot(x, w, label = 'White Noise (Mean = %s, Variance = %s)' % (round(mean_w, 2), round(var_w, 2)), color = 'b')
plt.plot(x, r, label = 'Red Noise (Mean = %s, Variance = %s)' % (round(mean_r, 2), round(var_r, 2)), color = 'r')
plt.legend()
plt.title('Oxygen Isotope delta-18O Data vs Noise')
plt.xlabel('Time')
plt.ylabel('delta-18O')
