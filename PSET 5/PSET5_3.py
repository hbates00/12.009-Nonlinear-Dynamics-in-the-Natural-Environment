# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 20:22:28 2017

@author: Haley
"""

import perc
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def largest_clusters(d, pc, lmax):
    
    length = range(2, lmax)
    size = np.array([0]*len(length))
    
    for i in xrange(10):
        clusters = perc.biggest_clusters(d, range(2, lmax), pc, 2)
        size += np.array([clusters[i][2][0] for i in xrange(len(clusters))])
    
    size = size/10.0
    
    return size
 
   
def plot_pc(d, pc, lmax):
    
    x = np.log(xrange(2, lmax))
    y = np.log(largest_clusters(d, pc, lmax))

    def func(x, a, b): #generates function to be fit against
        return a*x + b
    
    popt, pcov = curve_fit(func, x, y)

    print "a = %s , b = %s" % (popt[0], popt[1])
    
    plt.plot(x, func(x, *popt), label="Fitted Curve")
    
    plt.plot(x, y, label = 'Simulated Data (%s * x + (%s))'% (round(popt[0], 2), round(popt[1], 2)))
    plt.legend()
    plt.xlabel('Log of Grid Side Length L')
    plt.ylabel('Log of Size of Two Largest Clusters')
    plt.title('Size of Largest Clusters in 2D as a Function of Grid Size p = %s' % pc)


def plot_p_less(d, pc, lmax):
    
    x = np.log(xrange(2, lmax))
    y = largest_clusters(d, pc, lmax)

    def func(x, a, b): #generates function to be fit against
        return a*x + b
    
    popt, pcov = curve_fit(func, x, y)

    print "a = %s , b = %s" % (popt[0], popt[1])
    
    plt.plot(x, func(x, *popt), label="Fitted Curve")
    
    plt.plot(x, y, label = 'Simulated Data (%s * x + (%s))'% (round(popt[0], 2), round(popt[1], 3)))
    plt.legend()
    plt.xlabel('Log of Grid Side Length L')
    plt.ylabel('Size of Two Largest Clusters')
    plt.title('Size of Second Largest Clusters in 2D as a Function of Grid Size p = %s' % pc)    


def plot_p_more(d, pc, lmax):
    
    x = np.log(xrange(2, lmax))
    y = np.log(largest_clusters(d, pc, lmax))
    print x
    print y

    def func(x, a, b): #generates function to be fit against
        return a*x + b
    
    popt, pcov = curve_fit(func, x, y)

    print "a = %s , b = %s" % (popt[0], popt[1])
    
    plt.plot(x, func(x, *popt), label="Fitted Curve")
    
    plt.plot(x, y, label = 'Simulated Data (%s * x + (%s))'% (round(popt[0], 2), round(popt[1], 3)))
    plt.legend()
    plt.xlabel('Log of Grid Side Length L')
    plt.ylabel('Log of Size of Two Largest Clusters')
    plt.title('Size of Largest Clusters in %sD as a Function of Grid Size p = %s' % (d, pc))

plot_p_less(2, .57, 200)