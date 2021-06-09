# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 11:22:56 2021
Author: Roman Takhovskiy
zID: z5364695
Date: 1/1/2021


Program description:
    This program takes inputted altitude from user and determines in which layer is inputted altitude.

    
Data dictionary:
    Constants:
        TROPOSHERE_MIN = minimum altitude for troposhere: 0km
        TROPOSHERE_MAX = maximum altitude for troposhere: 17km (including 17km)
        
        STRATOSPHERE_MIN = minimum altitude for stratosphere: 17km (excluding 17km)
        STRATOSPHERE_MAX = maximum altitude for stratopshre: 60 km (including 60km)
        
        MESOSPHERE_MIN = minimum altitude for mesosphere: 60km (excluding 60km)
        MESOSPHERE_MAX = maximum altitude for mesosphere: 120km (including 120km)
        
        THERMO_MIN = minimum altitude for thermo and exosphere: 120km (excluding 120km)
        
    Variables:
        angle_bearing_list = list to store bearing angles
        angle_standard_list = list to store standard angles
"""

# Troposphere range
TROPOSHERE_MIN = 0
TROPOSHERE_MAX = 17 #including 17

# Stratosphere range
STRATOSPHERE_MIN = 17 #excluding 17
STRATOSPHERE_MAX = 60 #including

# Mesosphere range
MESOSPHERE_MIN = 60 #excluding 60
MESOSPHERE_MAX = 120 #including 120
 
# Thermo and exosphere range
THERMO_MIN = 120 #greater than 120


def classification (altitude):
    if altitude <= TROPOSHERE_MAX:
        print(f"Altitude of {altitude}km is Troposphere")
    elif altitude <= STRATOSPHERE_MAX:
        print(f"Altitude of {altitude}km is Stratosphere")
    elif altitude <= MESOSPHERE_MAX:
        print(f"Altitude of {altitude}km is Mesosphere")
    else:
        print(f"Altitude of {altitude}km is Thermo- and Exosphere")


classification(float(input("Please input your altitude to determine the altitude: ")))

