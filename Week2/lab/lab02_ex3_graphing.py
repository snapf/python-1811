# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 12:12:55 2021

@author: snapf
"""

#libraries
import math as m
import matplotlib.pyplot as plt


#constants
g = 9.8

#variables
v_init = 80
theta_init = m.pi/6
t_x = -70
t_y = -70
x_c = []
y_c = []

# x coordinate
while t_x < 80:
        x = v_init * m.cos(theta_init) * t_x
        t_x = t_x + 1
        x_c.append(x)
        

# y coordinate
while t_y < 80:
       y = v_init * m.sin(theta_init) * t_y - 0.5 * g * t_y**2
       t_y = t_y + 1
       y_c.append(y)

# graphing
plt.scatter(x_c,y_c)
plt.show()

