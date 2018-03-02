# -*- coding: utf-8 -*-
"""
Created on Wed May 03 16:42:02 2017

@author: Haley
"""

import numpy as np
from matplotlib import pyplot as plt

t = np.arange(0, 17520*10)
S_0 = 1361
#gamma = np.radians(23.5)
gamma = 0
P = 17520
phi = np.radians(42.5)

x_dot_n = []

for i in t: 
    lamb = (np.pi * (.5 * i - 12))/12
    delta = gamma * np.cos((2 * np.pi * i) / P)
    x_dot_n.append(max(S_0 * (np.cos(phi) * np.cos(lamb) * np.cos(delta) + np.sin(phi) * np.sin(delta)), 0))

x_dot_n = np.array(x_dot_n)
mean = np.sum(x_dot_n)/len(x_dot_n)
x_dot_n = x_dot_n[:] - mean

transform = np.fft.rfft(x_dot_n)

transform = np.abs(transform)**2

f = np.linspace(0, 24, np.size(transform))

plt.plot(f, transform)
plt.xlabel('Frequency 1/day')
plt.ylabel('Power')
plt.title('Power Spectrum of Insolation at %s Degrees Latitude (No Yearly Variations)' % (np.degrees(phi)))
