# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 14:50:26 2021

@author: snapf
"""
import numpy as np
import sim_projectile as sim
import matplotlib.pyplot as plt

# Problem parameters 
m = 0.145      # mass of the strawberry  
c = 0.0013     # damping coefficient 
v0 = 50        # initial launch speed
theta0d = 35   # initial launch angle 

# Simulation parameters 
time_start = 0           # start time 
time_end = 10            # end time 
time_increment = 0.01    # time increment 

time_array = np.arange(time_start,time_end + time_increment/2,
                          time_increment) # time array  
landing_level = 10

angle_array = np.arange(20,60,1)

len_time_array = len(time_array)
dt = time_array[1]-time_array[0]

landing_distance_array = np.zeros_like(angle_array, dtype="float")
landing_time_array = np.zeros_like(angle_array, dtype="float")

for k in range(len(angle_array)):
    position_x, position_y = sim.sim_projectile(time_array, m, c, v0, angle_array[k])
    landing_distance_array[k], landing_time_array[k] = sim.find_landing_pos_time(time_array,position_x,position_y,landing_level)
    
landing_distances_above_90 = np.where(landing_distance_array >= 90)

landing_angle = angle_array[np.min(landing_distances_above_90)]
print(landing_angle)

plt.plot(landing_time_array, landing_distance_array)
plt.show()