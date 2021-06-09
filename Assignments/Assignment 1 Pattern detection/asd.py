#  Script name: simulate_1d.py 
#  
#  Purpose: To simulate the position of the object with a 
#           particular pattern of movement 
#           (Version 1)
#  
#  Variable definitions:
#  dt        time increment for time array
#  time_end   end time of simulation
#  time_array   (vector) time 
#  pos_array    (vector) position 
#  pos0      initial position 
#  time_before  time in the previous simulation instance
#  velocity  velocity of the object 

# import libraries 
import numpy as np 
import matplotlib.pyplot as plt

#  Problem parameters 
#  Constants: Velocity profile 
TIME_LIMIT_1 = 0.4     #  Upper limit of time interval 1
TIME_LIMIT_2 = 0.8     #  Upper limit of time interval 2
VELOCITY_1 = 2         #  Velocity in time interval 1
VELOCITY_2 = -4        #  Velocity in time interval 2 
VELOCITY_3 = 1         #  Velocity in time interval 3  
#  Variables: 
dt = 0.1       #  time increment 
time_end = 1   #  end time 
pos0 = 1       #  initial position 

#  Time vector         
time_array = np.arange(0,time_end,dt)   

#  initialise storage for position vector x 
pos_array = np.zeros_like(time_array)
pos_array[1] = pos0  #  initial position 

#  the simulation loop
#  To be completed in the lecture 
for k in range(1,len(time_array)):
    #  Find the velocity in the previous time interval
    #  Find the previous time instance
    time_before = time_array[k-1]
    if time_before < TIME_LIMIT_1: 
        velocity = VELOCITY_1
    elif time_before < TIME_LIMIT_2:
        velocity = VELOCITY_2
    else:
        velocity = VELOCITY_3    
    #  Update pos_array(k) 
    pos_array[k] = pos_array[k-1] + velocity * dt  


#  Plot the position versus time 
plt.figure(1)
plt.plot(time_array,pos_array)
plt.grid()
plt.xlabel('x-position')
plt.ylabel('y-position')
plt.title('Position of the strawberry')
plt.show()