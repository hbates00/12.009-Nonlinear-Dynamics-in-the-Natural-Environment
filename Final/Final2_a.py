# -*- coding: utf-8 -*-
"""
Created on Wed May 17 15:48:58 2017

@author: Haley
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = []

with open('mass_coastline', 'r') as f:
    
    for line in f:
        n = line.split()
        n[0], n[1] = float(n[0]), float(n[1])
        
        data.append(n)

data = np.array(data)

x_coords = data[:, 0]
y_coords = data[:, 1]

min_x = min(x_coords)
max_x = max(x_coords)
min_y = min(y_coords)
max_y = max(y_coords)
print max_y

def matrix(r):
    
    x_length = np.ceil(max_x / float(r))
    #matrix[:, 0]
    y_length = np.ceil(max_y / float(r))
    #matrix[0, :]
    
    matrix = np.zeros((x_length, y_length))
    return matrix
    

def loop_it(r):
    
    grid = matrix(r)
    
    for i in data:
        x = i[0]
        y = i[1]
        
        x_grid = np.ceil(x / float(r)) - 1
        y_grid = np.ceil(y / float(r)) -1
        
        if grid[x_grid, y_grid] != 1:
            
            grid[x_grid, y_grid] = 1
            
        else:
            pass
    
    return grid
        

def all_together_now():
    r = np.array(range(250, 300, 5))
    n_r = np.zeros(len(r))
    
    for i in range(len(r)-1):
        
        n_r[i] = np.sum(loop_it(r[i]))
        
    return r, n_r

'''    
r, n_r = all_together_now()

def func(x, a, b):
    return a*x**b

popt, pcov = curve_fit(func, r, n_r)

a, b = popt[0], popt[1]
'''

plt.plot(r, n_r, label = 'N(r)')
plt.plot(r, func(r, *popt), label = "Fit %s * r ** %s" % (round(a, 2), round(b, 2)))
plt.xlabel('r (meters)')
plt.ylabel('N (number of boxes)')
plt.legend()
plt.title('Number of Boxes to Cover the Massachusetts Coastline as a Function of box Sidelength (Middling r)')
plt.xscale('log')
plt.yscale('log')



    
    



        
    
        
        
    
    


