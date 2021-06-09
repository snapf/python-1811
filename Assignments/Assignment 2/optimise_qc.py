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
      To Determine the discomfort levels for a given damper values and inerter values.
      The program initally determing the minimum number in discomfort array and determines
      where it is located on axis0 and axis1. Then calculates minimum number for inerter
      by using axis0 value in inerter array. Then it calculates minimum number for 
      damping coefficient by using axis1 value in damping coeefiecnt array.
      
      The program determines the maximum number in discomfort array which is below the 
      upper limite nd determines where it is located on axis0 and axis1. Then calculates 
      maximum number for inerter by using axis0 value in inerter array. Then it calculates 
      maximum number for damping coefficient by using axis1 value in damping coeefiecnt array.

   Description
   -----------
      This function finds 

   Data Dictionary
   ---------------
      a     acceleration
   
   Parameters
   ----------
      discomfort_array              2-dimentional numpy array with discomfort values for 
                                    given inerter_values and damping_coefficient_values (read the specs)    
      inerter_values                inertance values (array of type float)
      damping_coefficient_values    damping coefficient values (array of type float)
      discomfort_upper_limit        maximum discomfort value to calculate worst comfort
                                    (i.e. 'max_inerter' and 'max_damping_coefficient' values)
   
   Returns
   -------
      min_inerter and min_damping_coefficient  the pair that gives the smallest value of discomfort  
      max_inerter and max_damping_coefficient  the pair that gives the worst value of discomfort, that
                                             is less than or equal to a given 'discomfort_upper_limit'

""" 


import numpy as np

def optimise_qc(discomfort_array, inerter_array, damping_coefficient_array, discomfort_upper_limit):
   # Finding minimum number in discomfort array
   min_discormfort = np.min(discomfort_array)

   # determing minimum values for axis0 and axis1 of discomfort array
   min_axis0, min_axis1 = np.where(discomfort_array == min_discormfort)
   
   # Determining minimum number for inerter
   min_inerter = inerter_array[min_axis0]
   
   # Determining minimum number of damping coeffient
   min_damping_coefficient = damping_coefficient_array[min_axis1]
   
   # Determing max discormfort in discomfort array with discomfort upper limit
   max_discormfort = np.max(discomfort_array[discomfort_array <= discomfort_upper_limit])
   
   # Determining maximum values for axis0 and axis1 of discomfort array
   max_axis0, max_axis1 = np.where(discomfort_array == max_discormfort)
   
   # Determing maximum number of inerter
   max_inerter = inerter_array[max_axis0]
   
   # Determing maximum number of damping coeffient
   max_damping_coefficient = damping_coefficient_array[max_axis1]
   
   # returning the calculated results
   return min_inerter, min_damping_coefficient, max_inerter, max_damping_coefficient
