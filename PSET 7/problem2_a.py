# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 16:46:01 2017

@author: Haley
"""
import scipy
import numpy as np
from matplotlib import pyplot as plt

matdata = scipy.io.loadmat('HarvardForest.mat')
q_s = matdata['HarvardForest'][0, 0]['Solar_Rad'][0]

t = np.arange(0, 48*7)
year_data = q_s[:48*7]

plt.plot(t, year_data, label = 'Harvard Forest Data' )
plt.legend()
plt.xlabel('Time (half-hours)')
plt.ylabel('Insolation (Watts/m^2)')
plt.title('Insolation in a week in 1993 at the Harvard Forest')


    
