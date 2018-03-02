# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 19:30:42 2017

@author: Haley
"""

import perc
import matplotlib.pyplot as plt

def plot(l, p):

    grid = perc.percolation2d('biggest', l, p)
    
    plt.imshow(grid, cmap = "cool", interpolation = "nearest")
    
    cax = plt.imshow(grid, interpolation='nearest', cmap='cool')
    
    cbar = plt.colorbar(cax, ticks=[0, 1, 2])
    cbar.ax.set_yticklabels(['No Cluster', 'Small Clusters', 'Largest Cluster'])
    
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.title('Largest Cluster for p = %s' % p)
    
plot(1000, .5)