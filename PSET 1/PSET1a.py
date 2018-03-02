# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 16:21:25 2017

@author: Haley
"""

import scipy.io
import numpy as np
import matplotlib.pyplot as plt


matdata = scipy.io.loadmat('geyserdat.mat')
waittimes = matdata['Waitimes'].flatten()

print waittimes

m = 25

x1 = waittimes[:len(waittimes)-1]
y1 = waittimes[1:]

plt.scatter(x1, y1)
plt.xlabel('Index')
plt.ylabel('Index + 2')
plt.title('First Index Interval Time-Series vs Third Index Interval Time Series')

x2 = waittimes[:len(waittimes)-2]
y2 = waittimes[2:]

#plt.scatter(x2, y2)

def plot(m):

    plt.hist(waittimes, bins = m)
    plt.xlabel('Wait Time')
    plt.ylabel('Frequency of Wait Time')
    plt.title('Wait Times Between Geyser Eruptions')


s = 100000
num_samples = 100
sample_size = np.logspace(3, 5, num = num_samples, base = 10)
p = .1
m = 20
n = 50


def plot(s, p, m):

    tseries = np.random.rand(int(s)) <= p
    tvals = np.where(tseries)
    waits = np.diff(tvals)

    plt.hist(waits.T, bins = m)
    plt.xlabel('Wait Time')
    plt.ylabel('Frequency of Wait Time')
    plt.title('Wait Times Between Carbon 14 Atoms p = 5%')


def simulation(s, p):
    
    carbon14 = 0
    carbon12 = 0
    
    tseries = np.random.rand(int(s)) <= p
    
    carbon14 = np.count_nonzero(tseries)
    carbon12 = len(tseries) - carbon14

    return carbon14/float(carbon12)

def trials(s, p, n):
    xi = []
    
    for i in range(n):
        xi.append(simulation(s, p))
          
    return xi
        
def xbar(xi):
    return sum(xi) * (1 / float(n))
    
def sigma(s):
    
    xi = trials(s, p, n)
    x = xbar(xi)
    difference = []
    
    for i in xi:
        difference.append((i - x)**2)
    
    sigma = (1 / float(n - 1)) * sum(difference)
    return sigma

def sigma_range():
    
    variance = []
    
    for i in sample_size:
        variance.append(sigma(i))
    
    return variance

 
"""
y = sigma_range()
x = sample_size
plt.plot(x, y)
#plt.xscale('log')
#plt.yscale('log')
plt.xlabel('Sample Size')
plt.ylabel('Variance')
plt.title('Variance of Carbon 14 as a Function of Sample Size p = 0.5%')
"""
