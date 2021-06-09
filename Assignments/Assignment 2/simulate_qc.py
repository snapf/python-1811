#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
   Author
   ------
      Roman Takhovskiy (zID: 5364695)
   Date
   ----
      23/4/2021

   Purpose
   -------
      To calculate and simulate a quarter car based on the mathematical 
      models provided in assignments

   Description
   -----------
      This function simulates the quarter car based on the provided
      mathematical models provided in assignment. Initially program
      calculates the time increment (dt). Empty arrays based on
      time_array are created for ys, yu,vs, vu. The program uses
      assumption of vs[0] = yu[0] = vs[0] = vu[0] = 0. Then it 
      calculates equation (7) - (12) from assignment brief.

   Data Dictionary
   ---------------
      dt    time increment
   
   Parameters
   ----------
      time   time_array
      y_road  an array of road heights
      ms     the mass of 1/4 of the car body
      mu     the mass of the tyre and wheel
      kt     tyre stiffness
      k      spring stiffness
      b      inertance
      c      damping coefficient
   
   Returns
   -------
      ys     the verticle displacement of the center of the car body 
             from a reference level
      yu     the verticle displacement of the center of the wheel/tyre 
             from a reference level
      vs     the verticle velocity of the quarter car body       
      vu     the verticle velocity of the wheel/tyre

"""  

import numpy as np 
   

def simulate_qc(time_array, y_road, ms, mu, kt, k, b, c) : 

   # Calculates time increment (dt)
   dt = time_array[1] - time_array[0]
   # Calculates length of time array for a loop
   len_time_array = len(time_array) - 1
   
   # Initialising empty arrays based on time_array for 
   # ys, yu, vs, vu
   ys = np.zeros_like(time_array)
   yu = np.zeros_like(time_array)
   vs = np.zeros_like(time_array)
   vu = np.zeros_like(time_array)
   
   # Applying initial condition vs[0] = yu[0] = vs[0] = vu[0] = 0
   ys[0] = 0
   yu[0] = 0
   vs[0] = 0
   vu[0] = 0
      
   # For loop to calculate equations (7) - (12) for length of
   # time_array
   for i in range(len_time_array):
      # Calcuates equation (7)
      f_t = c*vs[i]-c*vu[i]+k*ys[i]-k*yu[i]
      # Calcuates equation (8)
      h_t = f_t - kt*yu[i]+kt*y_road[i]
      # Calcuates equation (9)
      ys[i+1] = ys[i]+vs[i]*dt
      # Calcuates equation (10)
      yu[i+1] = yu[i]+vu[i]*dt
      # Calcuates equation (11)
      vs[i+1] = vs[i]+((-(mu+b)*f_t+b*h_t)/(ms*mu+(ms+mu)*b))*dt
      # Calcuates equation (12)
      vu[i+1] = vu[i]+((-b*f_t+(ms+b)*h_t)/(ms*mu+(ms+mu)*b))*dt

   # returns calculated values
   return ys, yu, vs, vu 
    
 

