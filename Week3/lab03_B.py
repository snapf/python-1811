# -*- coding: utf-8 -*-
"""
Author: Roman Takhovskiy
zID: z5364695
Date: 28/2/2021


Program description:
    This program classifies triangles into equilaterial, isoceles and scalene based on their angle.

    
Data dictionary:
    Constants:
        TRIANGLE_ANGLE_SUM = triangle have angle sum of 180
        
    Variables:
        a,b,c = are the angles of the triangle.
        
"""


# Specify the angles
# a = 60; b = 60; c = 60;
# a = 70; b = 70; c = 40;
a = 40; b = 70; c = 70;
# a = 70; b = 40; c = 70; 
# a = 50; b = 70; c = 60; 


# Constants
TRIANGLE_ANGLE_SUM = 180

# Classification 
def classification(a, b, c):
     if a + b + c == TRIANGLE_ANGLE_SUM:
        if a == b and b == c and c == a:
            print(f"Equilateral triangle with angles: {a}, {b}, {c}")
        elif a == b or b == c or a == c:
            print(f"Isoceles triangle with angles: {a}, {b}, {c}")
        else:
            print(f"Scalene triangle with angles: {a}, {b}, {c}")
     else: 
        print(f"Angles {a} + {b} + {c} are not equal to {TRIANGLE_ANGLE_SUM} degrees,\
              therefore it is not a triangle")
        

classification(a,b,c)

        

            
