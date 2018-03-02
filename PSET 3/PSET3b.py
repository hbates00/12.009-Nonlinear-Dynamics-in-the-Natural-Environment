# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 16:08:13 2017

@author: Haley
"""
import scipy
import matplotlib.pyplot as plt


matdata = scipy.io.loadmat('ps3data.mat')

southpole_co2_t = matdata['SouthPole']['CO2'][0][0]['t'][0][0][0]
pointbarrow_co2_t = matdata['PointBarrow']['CO2'][0][0]['t'][0][0][0]
maunaloa_co2_t = matdata['MaunaLoa']['CO2'][0][0]['t'][0][0][0]

southpole_co2_v = matdata['SouthPole']['CO2'][0][0]['v'][0][0][0]
pointbarrow_co2_v = matdata['PointBarrow']['CO2'][0][0]['v'][0][0][0]
maunaloa_co2_v = matdata['MaunaLoa']['CO2'][0][0]['v'][0][0][0]

southpole_d13_t = matdata['SouthPole']['d13'][0][0]['t'][0][0][0]
pointbarrow_d13_t = matdata['PointBarrow']['d13'][0][0]['t'][0][0][0]
maunaloa_d13_t = matdata['MaunaLoa']['d13'][0][0]['t'][0][0][0]

southpole_d13_v = matdata['SouthPole']['d13'][0][0]['v'][0][0][0]
pointbarrow_d13_v = matdata['PointBarrow']['d13'][0][0]['v'][0][0][0]
maunaloa_d13_v = matdata['MaunaLoa']['d13'][0][0]['v'][0][0][0]


plt.plot(southpole_co2_t, southpole_co2_v, label = "South Pole")
plt.plot(pointbarrow_co2_t, pointbarrow_co2_v, label = "Point Barrow")
plt.plot(maunaloa_co2_t, maunaloa_co2_v, label = "Mauna Loa")

plt.xlabel('Time (Yr)')
plt.ylabel('C02 Amount (ppm)')

plt.title('Measurement of C02 from three stations')
plt.legend()

plt.show()

'''
plt.plot(southpole_d13_t, southpole_d13_v, label = "South Pole")
plt.plot(pointbarrow_d13_t, pointbarrow_d13_v, label = "Point Barrow")
plt.plot(maunaloa_d13_t, maunaloa_d13_v, label = "Mauna Loa")

plt.xlabel('Time (Yr)')
plt.ylabel('d13 Concentration')

plt.title('Concentration of carbon-13 from three stations')
plt.legend()

plt.show()
'''