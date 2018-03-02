# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 03:41:58 2017

@author: Haley
"""
import numpy as np
import matplotlib.pyplot as plt

def deviation(sigma, r):
    return ((1 / np.sqrt(2 * np.pi * sigma)) * np.exp(-(r**2) / (2 * sigma**2)))
    
x = range(-100, 100)
y = []
for i in x:
    y.append(deviation(20, i))

plt.plot( x, y)