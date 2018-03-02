# -*- coding: utf-8 -*-
"""
Created on Wed May 03 21:22:43 2017

@author: Haley
"""

import scipy
import numpy as np
from matplotlib import pyplot as plt

matdata = scipy.io.loadmat('HarvardForest.mat')
q_s = matdata['HarvardForest'][0, 0]['Solar_Rad'][0]

data = np.array(q_s)
mean = np.sum(data)/float(np.size(data))

data = data[:] - mean
transform1 = np.fft.rfft(data)
transform1= np.abs(transform1)**2

f1 = np.linspace(0, 24, np.size(transform1))


plt.plot(f1, transform1)
plt.xlabel('Frequency 1/day')
plt.ylabel('Power')
plt.xscale('log')
plt.title('Power Spectrum of Insolation at the Harvard Forest')
