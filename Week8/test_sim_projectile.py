#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 14:49:01 2017

@author: ctchou
"""
import numpy as np
import matplotlib.pyplot as plt
import sim_projectile as sim  

# Script name: testSimulateProjectile
#
# Purpose: This script is used to test whether the function
# simulateProjectile is working
#
# Variable definitions:
#   Variables for the problem: 
#       m           mass
#       c           drag coefficient
#       v0          initial total speed
#       theta0d     initial launch angle in degrees 
#
#   Variables for simulation 
#       dt              time increment 
#       time_end        end time for simulation 
#       time_array      (numpy array) time instances
#
#   Variables for the outcomes of the simulation
#       position_x   (numpy array) x-coordinates 
#       position_y   (numpy array) y-coordinates 
# 

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

print(time_array)
# Simulation to obtain the x- and y-positions
position_x,position_y = sim.sim_projectile(time_array,m,c,v0,theta0d)
# print(position_x)
# Plot y-position versus x-position 
plt.figure(1)
plt.plot(position_x,position_y)
plt.grid()
plt.xlabel('x-position')
plt.ylabel('y-position')
# plt.ylim(-150,25)
plt.title('Position of the strawberry')

plt.axhline(y=10, color='r', linestyle='-')
plt.axvline(x=96, color='r', linestyle='-')

# plt.show()
   
print(sim.find_landing_pos_time(time_array,position_x,position_y,10))
# print(sim.launch_angle())

# The following statement prints the graph to a file which you can insert
# in documents later on 
# plt.savefig("testPosXY.pdf") 

# launch_angle_list = np.arange(20,61,1)
  
# for k in range(len(launch_angle_list)):
#     position_x, position_y = sim.sim_projectile(time_array,m,c,v0,launch_angle_list[k])
#     landing_x, landing_t = sim.find_landing_pos_time(time_array, position_x,position_y, 10)
#     landing_distances[k] = landing_x
#     landing_times[k] = landing_t
    
# landing_distances_above_90 = np.where(landing_distances >= 90)

# landing_angle = launch_angle_list[np.min(landing_distances_above_90)]

# print(landing_angle)

    