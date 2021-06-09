#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 Lab 10

Template for Question 1  
"""

def q1_func(d,h,s):
    if d >0 and s > 0:
        if h >= 0:
            time = d/s + h/400
            if time < 4 and h < 200:
                answer = "Easy"
            elif time > 8 or h > 600:
                answer = "Hard"
            else:
                answer = "Medium"
    else:
        answer = "Invalid"
    
    return answer