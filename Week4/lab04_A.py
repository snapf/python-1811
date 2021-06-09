# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 14:16:50 2021

@author: snapf
"""

# H(z,a)
def proportion(z,a):
    h = z/(z + a)
    return h


# G(x,b,y,c)
def two_proportions(x,b,y,c):
    ratio_x = proportion(x,b)
    ratio_c = proportion(y,c)
    G = ratio_x * ratio_c
    return G, ratio_x, ratio_c



print(f"two proportions (z,a,x,b,y,c) are {two_proportions(2,6,2,6,5,35)}\n")

g, r1, r2 = proportion(2,6,5,35)

print(f"Value of g is {g},\nValue of r1 is {r1},\nValue of r2 is {r2}")
