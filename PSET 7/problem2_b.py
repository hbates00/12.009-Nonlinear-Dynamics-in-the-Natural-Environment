# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 18:11:11 2017

@author: Haley
"""
import scipy
import numpy as np
from matplotlib import pyplot as plt

matdata = scipy.io.loadmat('HarvardForest.mat')
q_s = matdata['HarvardForest'][0, 0]['Solar_Rad'][0]

t = np.arange(0, 17520)
S_0 = 1361
gamma = np.radians(23.5)
P = 17520
phi = np.radians(42.5)


x_dot_n = []
shift = np.radians((194.5/365) * 360)

for i in t: 
    lamb = (np.pi * (.5 * i - 12))/12
    delta = gamma * np.cos((2 * np.pi * i) / P)
    x_dot_n.append(max(S_0 * (np.cos(phi)*np.cos(lamb + shift)*np.cos(delta + shift) + np.sin(phi)*np.sin(delta + shift)), 0))
    
year_data = q_s[:(17520)]

plt.scatter(x_dot_n, year_data)
plt.xlabel('Theoretical I')
plt.ylabel('Harvard Forest Data')
plt.title('Comparison of Theoretical and Observed Insolation at the Harvard Forest')
plt.gca().set_xlim(left=0)
plt.gca().set_ylim(bottom=0)