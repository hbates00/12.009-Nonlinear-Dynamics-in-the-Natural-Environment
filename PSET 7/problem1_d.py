# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 17:18:51 2017

@author: Haley
"""
import numpy as np
from matplotlib import pyplot as plt


t = np.arange(0, 17520)
S_0 = 1361
gamma = np.radians(23.5)
P = 17520
phi = np.radians(90)


x_dot_n = []

for i in t: 
    lamb = (np.pi * (.5 * i - 12))/12
    delta = gamma * np.cos((2 * np.pi * i) / P)
    x_dot_n.append(max(S_0 * (np.cos(phi)*np.cos(lamb)*np.cos(delta) + np.sin(phi)*np.sin(delta)), 0))

print len(x_dot_n)

plt.plot(t, x_dot_n, label = 'latitude = %s' % (np.degrees(phi)))
plt.legend()
plt.xlabel('Time (half-hours)')
plt.ylabel('Insolation (Watts/m^2)')
plt.title('Insolation over a Year at Various Latitudes')
