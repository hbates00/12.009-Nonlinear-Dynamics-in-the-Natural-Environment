# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 22:32:53 2017

@author: Haley
"""
import numpy as np
from matplotlib import pyplot as plt


def u(alpha, delta, epsilon):
    
    theta = np.arange(0, 2*np.pi, .1)
    r = 1 / (alpha * (1 + epsilon * np.cos(theta - alpha * delta * theta)) + alpha**2 * delta * (1 + (epsilon**2/2) - (epsilon**2/6)* np.cos(2 * theta)))
    
    ax = plt.subplot(111, projection='polar')
    
    ax.plot(theta, r)
    ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
    ax.grid(True)
    
    ax.set_title("Radius of Orbit (alpha = %s, delta = %s, epsilon = %s)" % (alpha, delta, epsilon), va='bottom')
    plt.show()
    


u(.5, round(np.pi/40, 3), .5)
