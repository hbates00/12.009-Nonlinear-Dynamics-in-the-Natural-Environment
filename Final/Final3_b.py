# -*- coding: utf-8 -*-
"""
Created on Wed May 17 17:55:19 2017

@author: Haley
"""

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import random

data = []

with open('invperc_example', 'r') as f:
    
    for line in f:
        n = line.split()
        
        for i in range(len(n)):
            n[i] = int(n[i])
        
        data.append(n)

data = np.array(data)


def start():
    start = random.randrange(0, 999)
    return (start, 0)

def get_direction():
    return random.choice([[-1, 0], [1, 0], [0, 1], [0, -1]])

def is_adj(point, direction):
    
    x = (point[0] + direction[0]) % len(data[:, 0])
    y = point[1] + direction[1]
    
    if y < 0:
        return point
    elif y == len(data[0, :]):
        return point
    elif data[x, y] == 1:
        return [x, y]
    else:
        return point
    
def get_dist(point, start):
    x_point = point[0]
    y_point = point[1]
    x_start = start[0]
    y_start = start[1]
    
    dist = np.sqrt((x_point - x_start)**2 + (y_point - y_start)**2)
    
    return dist

def move_n_times(n):
    
    dist = []
    start_pos = start()
    old = start_pos
    new = ''
    
    for i in range(n):
        new = is_adj(old, get_direction())
        dist.append(get_dist(new, start_pos))
        old = new
    
    return np.array(dist)

def loopdidoo(n, simnum):
       
    global_dist = np.zeros(n)
    
    for i in range(1, simnum):
        distance = move_n_times(n)
        total = (global_dist + distance)
        
        global_dist = total
            
    return global_dist/float(simnum)

x_list = range(1000)
y_list = loopdidoo(1000, 15000)

def func(x, a, b):
    return a*x**b

popt, pcov = curve_fit(func, x_list, y_list)

a, b = popt[0], popt[1]

plt.plot(x_list, y_list, label = 'Simulated Partical Distance')
plt.plot(x_list, func(x_list, *popt), label = "Fit %s * t ** %s" % (round(a, 2), round(b, 2)))
plt.xlabel('Time')
plt.ylabel('Distance')
plt.title('Distance of a Particle from its Origin as a Function of Time')
plt.legend()
plt.xscale('log')
plt.yscale('log')









