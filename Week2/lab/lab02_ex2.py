# -*- coding: utf-8 -*-
"""
Author: Roman Takhovskiy
Date: 18/2/2021

Program description:
    The program calculates the number of complete revolution rotating disc at angular velocity of 621 has made and final the angular position of the red dot. 
    
    
Data dictionary:
    Constants:
        DEGREES_PER_REVOLUTION = degrees of revoltion is 360
        
    Variables:
        angular_speed = angular speed of 621
        time = time is 17.5
        complete_revolutions = calculates the complete revolutions
        angular_position = calculates the angular position of the dot
"""

# Constants
DEGREES_PER_REVOLUTION = 360

#variables
angular_speed = 621
time = 17.5

#degrees rotated
total_degrees = 621 * 17.5

#Number of completed revolutions
number_of_completed_revolutions = total_degrees//DEGREES_PER_REVOLUTION
print("Number of completed revolutions is: ", number_of_completed_revolutions)

#angular_position
#angular_position = total_degrees - number_of_completed_revolutions * DEGREES_PER_REVOLUTION
angular_position = total_degrees%DEGREES_PER_REVOLUTION
print("Angular position of red dot is: ", angular_position)