#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
     
    Purpose: To simulate a projectile given its mass (m), 
             drag coefficient (c), initial velocity v0 and
             its projectile angle theta0d in degrees

           
     Inputs: 
       time_array  (numpy array) time instants
       m           mass
       c           drag coefficient
       v0          initial total speed
       theta0d     initial launch angle in degrees 
    
     Outputs:
       position_x   (numpy array) x-coordinates 
       position_y   (numpy array) y-coordinates 
        
     Variable definitions:
     
     Simulation parameters:
       dt              time increment for time array
       len_time_array  number of time instants 
       velocity_x      (numpy array)  x-velocity
       velocity_y      (numpy array)  y-velocity 
"""
  
import numpy as np 
import math 

def sim_projectile(time_array,m,c,v0,theta0d): 
   
    # Constants 
    # Physical constants 
    g = 9.81   # acceleration due to gravity 
    
    # Extract information from time vector 
        # number of time points
    dt = time_array[1]-time_array[0]  # time increment 
    len_time_array = len(time_array)
    # Initialise storage for positions and velocities
    position_x = np.zeros_like(time_array)
    velocity_x = np.zeros_like(time_array)
    position_y = np.zeros_like(time_array)
    velocity_y = np.zeros_like(time_array)
    
    # initialise velocity at zero time 
    velocity_x[0] = v0*math.cos(math.radians(theta0d))
    velocity_y[0] = v0*math.sin(math.radians(theta0d))
    # initial position is assumed to be (0,0)
    
    # the simulation loop
    for k in range(len_time_array-1): 
        # Update x-position
        position_x[k+1] = position_x[k] + velocity_x[k] * dt  
        # Update y-position
        position_y[k+1] = position_y[k] + velocity_y[k] * dt
        
        # Compute total speed 
        speed_total = math.sqrt(velocity_x[k]**2+velocity_y[k]**2)
        # Update x-velocity
        velocity_x[k+1] = velocity_x[k] - c*speed_total*velocity_x[k]/m*dt
        # Update y-velocity
        
        velocity_y[k+1] = velocity_y[k] - (c/m*speed_total*velocity_y[k]+g)*dt 
  
    return position_x, position_y 

"""
find_landing_pos_time function

   Purpose: To determine the landing position and landing time 
            for a given landing level
    
    Inputs:
          time_array     (numpy array)  time 
          position_x     (numpy array)  x-coordinates 
          position_y     (numpy array)  y-coordinates  
          landing_level  desired landing level 
    
    Outputs:
          landing_position    The landing position is the x-coordinate at
                              the point where the y-coordinate is just
                              greater than the landing level and is falling
                              down
          landing_time        time at the landing_position 

   We use the last position which is just greater than landing level  
"""



def find_landing_pos_time(time_array,position_x,position_y,landing_level):
  # pos_max_index = np.argmax(position_y)
  # position = np.argwhere(position_y[pos_max_index] >= position_y[pos_max_index + 1] and position_y >= landing_level)
  # x = position_x[position]
  # last_pos = np.argwhere(x[len(x)-1] == position_x)
  # landing_position = position_x[last_pos]
  # landing_time = time_array[last_pos]


  landing_index = np.max(np.where(position_y >= landing_level))
  landing_time = time_array[landing_index]
  landing_position = position_x[landing_index]

  return landing_position, landing_time
