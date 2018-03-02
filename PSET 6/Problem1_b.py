# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 20:28:32 2017

@author: Haley
"""
import numpy as np
import matplotlib.pyplot as plt


def plotrange(tmax):
    t_range = np.arange(0, tmax, .2)
    
    for i in t_range:
        t = i

        z = np.arange(0, 6, .1)
        T = np.cos(t - z)*np.exp(-z)
        
        plt.plot(z, T, label = 'time = %s' % t)
        plt.legend()
        plt.title('Temperature as a Function of z')
        plt.xlabel('z distance')
        plt.ylabel('Temperature')

   
   
def plotone(period):
    z = np.arange(0, 6, .01)
    T = np.cos(1 - period * z)*np.exp(-z)
    e = np.exp(-z)
    eneg = -np.exp(-z)
    
    
    plt.plot(z, T, label = 'Temperature')
    plt.plot(z, e, label = 'Decay Envelope e^(-kx)', color = 'red')
    plt.plot(z, eneg, color = 'red')
    plt.legend()
    plt.title('Temperature as a Function of z')
    plt.xlabel('z distance')
    plt.ylabel('Temperature')
    
    
    
