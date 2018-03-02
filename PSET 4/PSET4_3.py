# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 17:12:19 2017

@author: Haley
"""

import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

xlimit = range(-50, 51)
ylimit = range(-50, 51)

# Finds a new direction for the walkers to move
def get_direction():
    return random.choice([[-1, 0], [1, 0], [0, 1], [0, -1]])

# Takes a list of the current position and a list of the direction to move and moves the walker
def add_move(position, move): 
    return [position[0] + move[0], position[1] + move[1]]

# Takes a list of the position of the current particle and a list of where all stuck particles are and returns if the current particle is stuck
def is_adjacent(pos, stuck): 
    a, b = pos[0], pos[1]  
    pos_adj = [ [a + 1, b], [a - 1, b], [a, b + 1] , [a, b - 1], [a + 1, b + 1], [a + 1, b - 1], [a - 1, b - 1], [a - 1, b + 1]]
    
    for i in pos_adj:    
        if i in stuck:
            return True
        else:
            pass
    return False

# Taks the position of the current particle and determines if it is in bounds
def bounds(pos):
    if pos[0] in xlimit and pos[1] in ylimit:
        return True
    else:
        return False

# Generates a random, valid initial position for a particle        
def initial_pos():
    status = random.choice([1, 2, 3, 4])
    if status == 1:
        return [xlimit[0], random.choice(ylimit)]
    elif status == 2:
        return [xlimit[len(xlimit) - 1], random.choice(ylimit)]
    elif status == 3:
        return [random.choice(xlimit), ylimit[0]]
    else:
        return [random.choice(xlimit), ylimit[len(ylimit) - 1]]

 #initiates a particle and moves it until it's stuck, replacing it at the edges if it is out of bounds or on top of another particle, returning the particle's position      
def aggregate(stuck):
    pos = initial_pos()
    while True:
        if bounds(pos) == True:
            if is_adjacent(pos, stuck) == False:
                move = get_direction()
                pos = add_move(pos, move)
            else:
                return pos
        else:
            pos = initial_pos()
            pass

# Takes a number of walkers and walks that many walkers until they are stuck. Returns the list of the positions of walkers.
def let_em_walk(n): 
    stucklist = [[0, 0]]
    a = 0
    while a < n:
        new_pos = aggregate(stucklist)
        if new_pos not in stucklist:
            stucklist.append(new_pos)
            a += 1
        else:
            pass
    return stucklist

def get_radius(stuck):
    radlist = []
    
    for i in stuck:
        radlist.append(np.sqrt(i[0]**2 + i[1]**2))
        
    return radlist

def get_plot_coords(stuck):
    x = []
    y = []
    for i in stuck:
        x.append(i[0])
        y.append(i[1])
    return x, y

def plot_distance(n):
    coord = let_em_walk(n)
    dist = get_radius(coord)
    dist.sort()
    
    plt.plot(dist)    
    plt.xlabel('Number of Walkers')
    plt.ylabel('Radius')
    plt.title('Number of Walkers at radius from center')
    plt.yscale('log')
    plt.xscale('log')


def plot_drunks(n):
    coord = let_em_walk(n)
    x, y = np.array(get_plot_coords(coord))
    z = np.sqrt(x**2 + y**2)
    
    scaled_z = (z - z.min()) / z.ptp()
    colors = plt.cm.spectral(scaled_z)
    
    plt.scatter(x, y, c = np.sqrt(x**2 + y**2), s = 20, edgecolors = colors)
    plt.xlim(xlimit[0], xlimit[len(xlimit) - 1])
    plt.ylim(ylimit[0], ylimit[len(ylimit) - 1])
    plt.title('Diffusion Limited Aggregation')
    plt.xlabel('x Position')
    plt.ylabel('y Position')
    plt.legend()
    plt.show()


coord = let_em_walk(200)
dist = get_radius(coord)
dist.sort()

y = dist
x = range(len(dist))

def func(x, a, b): #generates function to be fit against
    return a*x**(b)
    
popt, pcov = curve_fit(func, x, y)

print "a = %s , b = %s" % (popt[0], popt[1])
    
plt.plot(x, func(x, *popt), label="Fitted Curve (y = 0.5 * x^0.7)")
plt.plot(dist, label = "Simulated Curve")    
plt.xlabel('Number of Walkers')
plt.ylabel('Radius')
plt.title('Number of Walkers at radius from center')
plt.legend()
plt.yscale('log')
plt.xscale('log')





    
