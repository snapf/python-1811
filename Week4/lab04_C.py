"""
! * e = 5.5f (0 <= f <= 10)
! *   = f^2 -10f +55 (10 < f <= 20)

"""
import math as m
import matplotlib.pyplot as plt

# Constants
FORCE_MIN = 0
FORCE_MAX_1 = 10
FORCE_MAX_2 = 20
A = 5.5
B = 10
C = 55

# Function to calcuatae extension force
def e_calculation(f):
    if f <= FORCE_MAX_1:
        e = A * f
    else:
        e = f**2 - B*f + C
    return e


# input for force
input_force = float(input("please enter force: "))

# checking the range for input
if FORCE_MIN <= input_force <= FORCE_MAX_2:
    print(e_calculation(input_force))
else:
    input_force = float(input("please enter force between 0 and 20: "))

# input for step size
step_size = float(input("please enter stepsize: "))

# determine upper limit
upper_limit = m.floor(FORCE_MAX_2 / step_size) + 1

# calculate the force list
force_list = [step_size * i for i in range(0, upper_limit)]

# calculate the extension
e_list = [e_calculation(j) for j in force_list]

#plot
plt.plot(force_list,e_list)
plt.grid(True)
plt.show()
