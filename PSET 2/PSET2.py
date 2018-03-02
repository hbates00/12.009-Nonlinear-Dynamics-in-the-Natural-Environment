# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 18:02:16 2017

@author: Haley
"""
import numpy as np
import matplotlib.pyplot as plt

D = 2e-5
qstar = .005
H = 1.005



x = np.arange(0, 5000, 100)
y1 = np.sqrt(((D * x * qstar * (H-1))/1000) + (.000001)**2)
y2 = np.sqrt(((D * x * qstar * (H-1))/1000) + (.00001)**2)
y3 = np.sqrt(((D * x * qstar * (H-1))/1000) + (.0001)**2)

plt.plot(x, y1, label = 'Starting Radius = 1e-6m')
plt.plot(x, y2, label = 'Starting Radius = 10e-6m')
plt.plot(x, y3, label = 'Starting Radius = 100e-6m')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xscale('log')
plt.yscale('log')

plt.ylabel('Radius of Droplet (m)')
plt.xlabel('Time (s)')
plt.title('Radius of a Droplet Detail')
plt.show()