# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 10:31:43 2017

@author: Haley
"""
import numpy as np
import matplotlib.pyplot as plt

def this_time(t, repeat):
    yes = 0.0
    
    for r in xrange(repeat):
        posx = 0
        posy = 0
        for i in xrange(t):
            if np.random.choice([-1, 1]) == 1:
                posx += np.random.choice([-1, 1])
            else:
                posy += np.random.choice([-1, 1])
            
            if posx == 0 and posy == 0:
                yes += 1.0
                break
            else:
                pass

    return (1.0- (yes/(float(repeat))))
   
def all_times(t, repeat):
    probs = []
    
    for i in range(t):
        probs.append(this_time(i, repeat))
        
    return probs

y = all_times(200, 500)
x = range(200)


plt.plot(y, label = "Simulated Probability Data")
plt.title('Probability of a Random Walker Never Returning to Origin in 2D')
plt.xlabel('Time Steps')
plt.ylabel('Probabilty')
plt.xscale('log')
plt.yscale('log')
plt.legend()