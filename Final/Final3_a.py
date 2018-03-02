# -*- coding: utf-8 -*-
"""
Created on Tue May 16 20:46:05 2017

@author: Haley
"""

import numpy as np
import matplotlib.pyplot as plt
import invperc
from scipy.optimize import curve_fit

x_range = range(5, 500, 5)

def get_thing():
    
    r = []
    
    for i in x_range:
        
        n = []
        
        for j in range(5):
            n.append(invperc.invperc(i))
        
        value = np.mean(n)
        r.append(value)
        
    return r

r = get_thing()

def func(x, a, b):
    return a*x**b

popt, pcov = curve_fit(func, x_range, r)

a, b = popt[0], popt[1]

plt.plot(x_range, r, label = "Simulated Oil Volume")
plt.plot(x_range, func(x_range, *popt), label = "Fit %s * L ** %s" % (round(a, 2), round(b, 2)))
plt.title("Displaced Volume of Oil as a Function of Side Length")
plt.xlabel("Side Length of Grid")
plt.ylabel("Volume of Oil Displaced")
plt.xscale('log')
plt.yscale('log')
plt.legend()