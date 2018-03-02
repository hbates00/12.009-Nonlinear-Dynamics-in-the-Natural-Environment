# -*- coding: utf-8 -*-
"""
Created on Wed May 03 18:03:56 2017

@author: Haley
"""

import scipy
import numpy as np
from matplotlib import pyplot as plt

matdata = scipy.io.loadmat('geysertimeseries.mat')
g = matdata['geysertimeseries'][:, 0]

data = np.array(g)
mean = np.sum(data)/float(np.size(data))

data = data[:] - mean
transform = np.fft.rfft(data)
transform = np.abs(transform)**2

f = np.linspace(0, .5, np.size(transform))

plt.plot(f, transform)
plt.xlabel('Frequency 1/hour')
plt.ylabel('Power')
plt.title('Power Spectrum of Geyser Eruption')
