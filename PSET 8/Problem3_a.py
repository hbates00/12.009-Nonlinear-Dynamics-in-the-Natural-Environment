# -*- coding: utf-8 -*-
"""
Created on Wed May 03 18:30:04 2017

@author: Haley
"""

import scipy
import numpy as np
from matplotlib import pyplot as plt

matdata = scipy.io.loadmat('vostok.mat')
g = matdata['OxygenIsotopesd18O'][0]

data = np.array(g)
mean = np.sum(data)/float(np.size(data))

data = data[:] - mean
transform = np.fft.rfft(data)
transform = np.abs(transform)**2

f = np.linspace(0, .5, np.size(transform))

plt.plot(f, transform, color = 'k')
plt.xlabel('Frequency 1/1000yrs')
plt.axvline(x = .01, label = 'Combined Eccentricity Frequency', color= '#ef1010', linestyle='--')
plt.axvline(x = .0388, label = 'Axial Precession Frequency', color='#ff6600', linestyle='--')
plt.axvline(x = .02439, label = 'Axial Tilt (Obliquity) Frequency', color='#bc9d00', linestyle='--')
plt.axvline(x = .00242, label = 'Component 1 of Eccentricity Frequency', color='#25c910', linestyle='--')
plt.axvline(x = .0105, label = 'Component 2 of Eccentricity Frequency',color='#047a4d', linestyle='--')
plt.axvline(x = .008, label = 'Component 3 of Eccentricity Frequency', color='#04c2cc', linestyle='--')
plt.axvline(x = .0025, label = 'Beat Period of Eccentricity Frequency', color='#042fcc', linestyle='--')
plt.axvline(x = .008928, label = 'Apsidal Precession Frequency', color='#6708db', linestyle='--')
plt.axvline(x = .014285, label = 'Orbital Inclination Frequency', color='#b700b7', linestyle='--')
plt.legend()
plt.xscale('log')
plt.ylabel('Power')
plt.title('Power Spectrum of Glacial d18_O')
