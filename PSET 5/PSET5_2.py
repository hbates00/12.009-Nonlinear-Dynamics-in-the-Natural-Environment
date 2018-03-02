# -*- coding: utf-8 -*-
"""
Created on Wed Apr 05 16:21:01 2017

@author: Haley
"""

import perc
import matplotlib.pyplot as plt
import numpy as np


def percent_largest(d, lmax):
    
    p = .01
    q = []
    
    while p <= 1:
        size = 0
        total = 0
        
        for i in xrange(10):
            size += perc.biggest_clusters(d, lmax, p, 1)[0][2][0]
            total += ((lmax**2) * p)
        
        size1 = size/10.0
        total1 = total/10.0
        
        p += .01
        
        q.append(size1/total1)
        
    return q
    
def percent_second_largest(d, lmax):
    
    p = .01
    q = []
    
    while p <= 1:
        size = 0
        total = 0
        
        for i in xrange(10):
            size += perc.biggest_clusters(d, lmax, p, 2)[0][2][1]
            total += ((lmax**2) * p)
        
        size1 = size/10.0
        total1 = total/10.0
        
        p += .01
        
        q.append(size1/total1)
        
    return q

def plot(d, l):
    
    a = percent_largest(d, l)
    b = percent_second_largest(d, l)
    x = np.arange(.01, 1, .01)
    
    plt.plot(x, a, label = 'q_1')
    plt.plot(x, b, label = 'q_2')
    plt.legend()
    plt.xlabel('Probability p')
    plt.ylabel('Log of Probability q')
    plt.yscale('log')
    plt.title('Probability a Randomly Chosen Point is Part of the Two Largest Clusters in %sD' % d)
    
plot(3, 30)


            
        