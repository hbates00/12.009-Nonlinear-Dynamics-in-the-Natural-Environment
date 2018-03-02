# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 18:28:10 2017

@author: Haley
"""
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

radius = .1 #in cm

def randCoord(): #returns a vector of form <x, y, z>
    return [random.uniform(-radius/2, radius/2), random.uniform(-radius/2, radius/2), random.uniform(-radius/2, radius/2)]
        
def newDirection(): #returns new cartesian coordinates normalized to length .1  
    r = 1
    
    while r > radius:
        coord = randCoord()
        x = coord[0]
        y = coord[1]
        z = coord[2]
        r = np.sqrt(x**2 + y**2 + z**2)

    return [x / (10 * r), y / (10 * r), z / (10 * r)]

def distance(d): #takes a vector and returns distance from center of sun
    
    return np.sqrt(d[0]**2 + d[1]**2 + d[2]**2)
    
def move(d): #takes current coordinate and adds movement coordinate, returns new coordinate
    i = newDirection()
    
    return [d[0] + i[0], d[1] + i[1], d[2] + i[2]]
    
def walk(p): #takes a given distance from sun and returns number of steps to get there
    
    position = [0, 0, 0]
    count = 0
    d = 0
    
    while d < p:
        
        position = move(position)
        d = distance(position)
        count += 1
        
    return count
    
def simulate(n, d): #takes a number of photons and a distance and finds the average amount of steps to reach that distance
    
    steps  = 0
    
    for i in xrange(0, n):
        steps += walk(d)
    
    return steps / n
        
'''
commenting out so it doesn't need tp run every time

dist1 = simulate(300, 1)
print dist1
dist2 = simulate(300, 2)
print dist2
dist3 = simulate(300, 3)
print dist3
dist4 = simulate(300, 4)
print dist4
dist5 = simulate(300, 5)
print dist5
dist10 = simulate(300, 10)
print dist10
dist20 = simulate(300, 20)
print dist20
'''

#values found from commented section above -----
dist1 = 114
dist2 = 498
dist3 = 917
dist4 = 1753
dist5 = 2324
dist10 = 10363
dist20 = 46669
#--------


x = [1, 2, 3, 4, 5, 10, 20]
y = [dist1, dist2, dist3, dist4, dist5, dist10, dist20]

x = np.array(x, dtype = "float")
y = np.array(y, dtype = "float")

plt.plot(x, y, label = "Simulated Data")

def func(x, a, b): #generates function to be fit against
    return a*x**(b)
    
popt, pcov = curve_fit(func, x, y)

print "a = %s , b = %s" % (popt[0], popt[1])
    
plt.plot(x, func(x, *popt), label="Fitted Curve (y = 73.73 * x ** 2.15)")


plt.xscale('log')
plt.yscale('log')

plt.xlabel('Distances (cm)')
plt.ylabel('Average Steps Taken')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.title('Average Steps Required for a Photon to Reach a Given Distance')
plt.show()
