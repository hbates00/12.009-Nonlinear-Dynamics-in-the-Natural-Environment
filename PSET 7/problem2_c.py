# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 16:50:09 2017

@author: Haley
"""

e of import numpy as np
import scipy.io.wavfile as siw
import scipy

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

'''
maxx = max(year_data)
minx = min(year_data)

sound_dat = []

for i in xrange(0, len(year_data)-1):
    x = year_data[i]
    newx = 2*((x - minx)/(maxx - minx)) - 1
    sound_dat.append(float(newx))
    
siw.write('forest.wav', 8192, np.array(sound_dat))

'''

sound_dat = []

maxx = max(x_dot_n)
minx = min(x_dot_n)    

for i in xrange(0, len(x_dot_n)-1):
    x = x_dot_n[i]
    newx = 2*((x - minx)/(maxx - minx)) - 1
    sound_dat.append(float(newx))


siw.write('theoretical.wav', 8192, np.array(sound_dat))
