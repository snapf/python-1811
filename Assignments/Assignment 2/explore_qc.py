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
      To calculate the discomfort levels for a given damper values and
      inerter values.

   Description
   -----------
      This function calculates discomfort levels by calculating vs values
      by using simulate_qc and calculates discomfort levels by using 
      calc_discomfort to calculate discomfort.

   Data Dictionary
   ---------------
      len_axis1   length of inerter_array
      len_axis0   length of damping_coefficient_array
   
   Parameters
   ----------
      time   time_array
      y_road  an array of road heights
      ms     the mass of 1/4 of the car body
      mu     the mass of the tyre and wheel
      kt     tyre stiffness
      k      spring stiffness
      inerter_values              inertance values (array of type float)
      damping_coefficient_values  damping coefficient values (array of type float)
   
   Returns
   -------
      discomfortLevels     2-dimentional numpy array with discomfort values for 
                           given damper values and inerter values (read the specs)

""" 

import numpy as np
import calc_discomfort as cd
import simulate_qc as sqc


def explore_qc(time_array, y_road, ms, mu, kt, k, inerter_array, damping_coefficient_array):
   # Calculates the length of inerter_array and stores as len_axis1
   len_axis1 = len(inerter_array)
   # Calculates the length of damping_coefficient_array and stores as len_axis0
   len_axis0 = len(damping_coefficient_array)

   # Creates an array with length of len_axis1 and len_axis0 with date type of float
   discomfortLevels = np.zeros((len_axis1, len_axis0), dtype = float)

   # For loop to calculate discomfortLevels
   for i in range(len_axis1):
      for j in range(len_axis0):
         # uses simulate_qc to calculate vs
         ys, yu, vs, vu = sqc.simulate_qc(time_array, y_road, ms, mu, kt, k, inerter_array[i], damping_coefficient_array[j])
         # Calculates discomfort levels by using vs and calc_discomfort
         discomfortLevels[i,j] = cd.calc_discomfort(vs,time_array[1] - time_array[0])
   # Returns discomfortLevels
   return discomfortLevels

