# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 15:29:12 2021

@author: snapf
"""
import math
import matplotlib.pyplot as plt

# constants
g = 9.81

def free_fall (m, d, t):
    v = (g*m/d) * (1-math.exp(-d/m*t))
    return v

m = 70          # mass
d = 12.5        # drag coefficient


t = []
sum_ = 0
while sum_ <= 40:
    t.append(sum_)
    


