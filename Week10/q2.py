#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Lab 10

Template file for Question 2 
"""
# Import numpy
import numpy as np 

def q2_func(x,y):
    z = np.zeros_like(x)
    z = np.where(np.abs(x) > np.abs(y),x - y/2, y-x/2)
    return z

    