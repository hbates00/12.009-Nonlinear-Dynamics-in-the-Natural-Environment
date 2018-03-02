# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 16:43:08 2017

@author: Haley
"""

#numpy random, generate list of random 1 or neg 1 and sum to get a number -- this is position
import numpy as np
import matplotlib.pyplot as plt


# Gets location after number of steps n and returns a location
def get_location(t):
    choice = np.array([-1, 1])
    moves = np.random.choice(choice, t)
    
    return np.sum(moves)

# Builds a vector of walker position  
def do_the_thing(n, t):
    a = map(lambda p: get_location(t), range(n))
    return a
    
# Creates and populates an rxr A matrix
def matrix(r):
    mat = np.zeros((r, r))
    
    for i in xrange(r):
        for j in xrange(r):
            if j == (i + 1) or j == (i - 1):
                mat[i][j] = .5    
            else:
                pass  
    return mat

# Advances a given number of time steps, returns a vector of probabilities  
def do_it(r, t):
    
    t_0 = np.array([0] * r)
    t_0[len(t_0)/2.0] = 1
    
    A = np.linalg.matrix_power(matrix(r), t)
    b = np.dot(A, np.transpose(t_0))
    return b
    
# Plots a histagram of walker locations
def plot(n, t, b):
    pos = do_the_thing(n, t)
    
    plt.hist(pos, bins = b, color = 'white', label = 'Simulated Values')    

# Plots the probability histogram
def plot_probabilities(n, t, r):
    
    probs = do_it(r, t) * 2 * n
    x = range((-r/2), (r/2))
    
    plt.plot(x, probs, label = 'Predicted Values')

plot(50000, 50, 15)
plot_probabilities(50000, 50, 50)
   

plt.xlabel('Position')
plt.ylabel('Number of Walkers at Position')
plt.title('Number of Random Walkers at Position After 50 Steps')
plt.legend()
plt.show()