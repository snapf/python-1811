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
      To calculate the discomfort array based on the given vehicle
      and suspension parameters

   Description
   -----------
      This function calculates the discomfort by calculating accelerate
      at each time instances (a[i] = ( vs[i+1] - vs[i] ) / dt). Discormfort
      is equal to the sum of all acceleration values squared.

   Data Dictionary
   ---------------
      a     acceleration
   
   Parameters
   ----------
      vs    the verticle velocity of the quarter car body       
      dt    time increment 
   
   Returns
   -------
      discomfort     a scalar representing the discomfort level for the given
                     vehicle and suspension parameters

""" 
# import numpy
import numpy as np

def calc_discomfort(vs , dt):
   # Initialising empty array based on vs array for accelaration
   a = np.zeros_like(vs)
   # Calculating the acceleration using a[i] = ( vs[i+1] - vs[i] ) / dt
   a = np.diff(vs/dt)
   # Calculating the discormfort by squaring each acceleration value
   # and adding them together
   discomfort = np.sum(a**2)
   
   # returning discomfort value
   return discomfort


