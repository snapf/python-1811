# -*- coding: utf-8 -*-

"""
Author: Roman Takhovskiy
zID: z5364695
Date: 26/2/2021


Program description:
    This program converts bearing angle to standard angles and graphs the bearing angle against 
    standard angle.

    
Data dictionary:
    libraries:
        - pandas
        - matplotlib.pyplot

    Constants:
        INPUT_MIN = is the minimum value of bearing
        INPUT_MAX = is the maximum value of bearing
        
    Variables:
        angle_bearing_list = list to store bearing angles
        angle_standard_list = list to store standard angles
        
"""



# libraries
import matplotlib.pyplot as plt
import pandas as pd




# function for bearing conversion
def bearing_conversion(bearing):
    if 0 <= bearing < 270:
        angle_standard = 90 - bearing
    else:
        angle_standard = 450 - bearing
    
    return angle_standard


# Input range variables
INPUT_MIN = 0
INPUT_MAX = 360


# user input for bearing
angle_bearing = int(input("Please enter your bearing angle: "))

# Test if input value in proper range 
if INPUT_MIN <= angle_bearing <= INPUT_MAX:
    print(f"Your inputed angle is: {bearing_conversion(angle_bearing)}")
else:
    print("You need to enter angle in [0, 360]")
    angle_bearing = int(input("Please enter your bearing angle: "))

print("\n")



angle_bearing_list = [0, 60, 90, 150, 180, 240, 269, 270, 310, 360]
angle_standard_list = []




# loop to convert the bearing angles to standard angles
for i in angle_bearing_list:
    angle_standard_list.append(bearing_conversion(i))



print("Bearing", angle_bearing_list)
print("Angle", angle_standard_list)
print("\n")



# creating table
table = pd.DataFrame({'Bearing: ': angle_bearing_list, 'Angle: ': angle_standard_list})
print(table)
print("\n")




#Graphing

# size of plot
plt.figure(figsize=(12, 10))

# plotting scatter plot
plt.scatter(angle_bearing_list, angle_standard_list)

# adding title
plt.title("Relationship between bearing angles and standard angles", fontsize=20, y=1.01)

# adding labels
plt.xlabel("Bearing Angle", fontsize=16, labelpad=14)
plt.ylabel("Standard Angle", fontsize=16, labelpad=14)

# set the limit of x and y axis:
plt.xlim(-1, 400)
plt.ylim(-200,200)

plt.show()


# Calculating straight lines