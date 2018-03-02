# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:44:34 2017

@author: Haley
"""
import numpy as np
import matplotlib.pyplot as plt


def matrix(r):
    mat = np.zeros((r, r))
    
    for i in xrange(r):
        for j in xrange(r):
            if i == 0:
                mat[i][j] = 0
            elif i == (r - 1) and j == (r - 1):
                mat[i][j] = 1
            elif j == (i + 1) or j == (i - 1):
                if i != (r - 1):
                    mat[i][j] = .5    
                else:
                    pass
            else:
                pass  
    return mat
    
def do_it(r, t):
    
    t_0 = np.array([1] * r)
    
    A = np.linalg.matrix_power(matrix(r), t)
    b = np.dot(A, np.transpose(t_0))
    
    return b

def build_heatplot(r, t):
    
    a = do_it(r, t)
    matrix = [a] * r
    matrix = np.array(matrix)
    
    return matrix.T

def find_flux(r, t):
    
    a = do_it(r, t)
    flux = []
    
    for i in range(len(a)):
        if i + 1 >= len(a):
            return flux
        else:
            flux.append(a[i + 1] - a[i])
    return flux
        
print find_flux(20, 1000)

a = build_heatplot(20, 1000)
plt.imshow(a, cmap='hot', interpolation='nearest')
plt.title('Temperature of Seafloor Slab t = 1000')
plt.xlabel('X Position')
plt.ylabel('Z Position')
plt.colorbar(cmap = 'hot')
plt.show()
