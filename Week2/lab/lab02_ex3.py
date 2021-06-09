# -*- coding: utf-8 -*-
"""
Author: Roman Takhovskiy
Date: 18/2/2021

Program description:
    This program calculates the x and y coordintes on a projectile at givien time using projectile equations:
        
        x(t)=vcos(theta)t

        y(t)=vsin(theta)t-0.5gt^2

    
Data dictionary:
    libraries:
        math

    Constants:
        g = Earth's gravitational acceleration, 9.8 m/s/s
        
    Variables:
        v_initial = intial velocity, 80
        theta_initial = initial angle of projectile, pi/6
        t = time, 5
"""

#libraries
import math as m


#constants
g = 9.8

#variables
v_initial = 80
theta_initial = m.pi/6
t = 5

# x coordinate
x = (v_initial * m.cos(theta_initial) * t)
print("x coordinate is: ", x)

# y coordinate
y = v_initial * m.sin(theta_initial) * t - 0.5 * g * t**2
print("y coordinate is: ", y)

