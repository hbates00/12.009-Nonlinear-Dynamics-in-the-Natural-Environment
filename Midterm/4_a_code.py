# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 04:02:14 2017

@author: Haley
"""
import numpy as np
import matplotlib.pyplot as plt


def this_time(t, repeat):
    yes = 0.0
    
    for r in xrange(repeat):
        pos = 0
        for i in xrange(t):
            pos += np.random.choice([-1, 1])
            if pos == 0:
                yes += 1.0
                break
            else:
                pass

    return (1.0- (yes/(float(repeat))))
    
def all_times(t, repeat):
    probs = []
    
    for i in range(t):
        probs.append(this_time(i, repeat))
        
    return probs

y = all_times(100, 500)
x = range(100)
'''
def func(x, a, b): #generates function to be fit against
    return a * x **(-b)
    
popt, pcov = curve_fit(func, x, y)

x1 = range(100)
y1 = []

for i in x1:
    y1.append(func(i, *popt))

print "a = %s , b = %s" % (popt[0], popt[1])
    
plt.plot(x1, y1, label="Fitted Curve (y = 0.84 * e ** (0.18 * x) + 0.088)")
'''
plt.plot(y, label = "Simulated Probability Data")
plt.title('Probability of a Random Walker Never Returning to Origin in 1D')
plt.xlabel('Time Steps')
plt.ylabel('Probabilty')
plt.xscale('log')
plt.yscale('log')
plt.legend()
