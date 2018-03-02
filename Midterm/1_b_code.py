# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 19:26:21 2017

@author: Haley
"""
import matplotlib.pyplot as plt
import random

# takes in the position of a walker and moves it up or down with a 50/50 chance.
def move_walker(pos):
    position = pos
    if random.uniform(0, 1) <= 0.5:
        position -= 1
    else:
        position += 1
        
    return position


# deletes walkers based on probability, or if their position is positive (they have left the microbial mat)    
def delete_walkers(walkers, p, zero_num):
    
    for i in walkers[:]:
        
        if random.uniform(0, 1) <= p:
            walkers.remove(i)    
    
    for i in walkers[:]:
        if i <= 0:
            walkers.remove(i)
        else:
            pass
        
    return walkers + [0] * zero_num


# takes time step, probability of uptake, and number of walkers at z = 0 and moves walkers
def go(t, p, n):
    walkers = [0] * n
    
    for i in xrange(t):
        for i in xrange(len(walkers)):
            pos = walkers[i]
            walkers[i] = move_walker(pos)
        
        walkers = delete_walkers(walkers, p, n)
    return walkers

def plot_it(t, p, n, b):
    
    plt.hist(go(t, p, n), bins = b)
    plt.xlabel('Position')
    plt.ylabel('Carbon Dioxide Molecules at Position')
    plt.title(('Uptake of Carbon Dioxide in Microbial Mat p = '+ str(p)))

plot_it(1000, .5, 100, 4)