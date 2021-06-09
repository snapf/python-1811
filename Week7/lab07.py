# Import packages
import numpy as np
import matplotlib.pyplot as plt

# Load data and store it as a numpy array called data_sea_ice
data_sea_ice = np.loadtxt(fname="sea_ice.txt")

# Check the shape of the numpy array
print("The shape of the numpy array is: ", data_sea_ice.shape)

# The shape of the array is 35 x 25
# number of rows = number of years
# Each row has 25 elements:
# The first element is the year, followed by 24 measurements per year (i.e. 1 measurement per half a month)

# Print out the first row to confirm the data format
print("The first row of data is \n", data_sea_ice[0,:])

# We need to move the years into a different variable and then remove the years from the first column
years = data_sea_ice[:,0];   # first column, easy
data_sea_ice = np.delete(data_sea_ice, 0, axis=1)   # remove the first column
print("The shape of the numpy array is: ", data_sea_ice.shape)  # should be 35 (years) x 24 (half-monthly samples)

avg1 = np.average(data_sea_ice, axis = 1)
print(avg1)

# The following line uses a numpy function to produce the array: array([0.5, 1, 1.5, 2, ..., 11.5, 12])
months = np.linspace(0.5,12,24)
# We haven't discussed linspace yet but for this lab, it is sufficient for you to know what the contents of the numpy array months are
# If you want to know more about the numpy function linspace, its manual page is at
#  https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.linspace.html#numpy.linspace

# plot the data - you should add the xlabel, ylabel, title
# You will see 35 curves, each curve depicts the variation of sea ice extents in one year
# The seasonal variation should be obvious and don't forget, the data came from the northern hemisphere  
# You will need to plot more figures later on, so put it in Figure 1
plt.figure(1)
plt.plot(months, np.transpose(data_sea_ice))
plt.xticks([2, 4, 6, 8, 10, 12], ["Feb", "Apr", "Jun", "Aug", "Oct", "Dec"])  # This shows you how to use xticks
plt.show()