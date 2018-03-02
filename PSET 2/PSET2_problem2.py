# -*- coding: utf-8 -*-
"""
Created on Wed Mar 01 23:53:05 2017

@author: Haley
"""

import matplotlib.pyplot as plt
import numpy as np

D = 2e-7
Q = 10
C = 10**6
a = .008
K = np.sqrt((Q * a)/(C * D))
L = np.sqrt((C * D)/(Q * a))

H = 20


x = np.arange(-H, H, .1)

y1 = (Q * (H**2 - x**2))/(2*D*C)
y2 = (1/(np.cos(K*H)*a))*np.cos(K*x) - 1/a

plt.plot(x, y1, label = "Constant Decomposition Rate")
plt.plot(x, y2, label = "Linear Decomposition Rate")
plt.xlabel('Vertical Distance')
plt.ylabel('Temperature')

plt.title('Thermal Diffusion in a Compost Pile (unrealistically large alpha)')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


