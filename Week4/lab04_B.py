# libarries
import matplotlib.pyplot as plt
import pandas as pd

# creating x-coordinate list
x = [i for i in range(2,13,2)]

# creating y-coordinate list
y = [k**2 for k in x]

# creating table
print(pd.DataFrame({'x-axis: ': x, 'y-axis: ': y}))

# Graphing part 1
plt.plot(x,y)        
plt.grid(True)
plt.xlabel("range 2:12")
plt.ylabel("square of x-axis")
plt.show()


# print([1,2] * 4) prints [1,2] 4x times
# print(3 * [2,4,5]) prints [2,4,5] 3x times
# print([10] + [23,15,66] + [-3, -5]) adds 3 lists together in 1 list



pt3_x = list(range(8))
pt3_y = [3] * len(pt3_x)
# plt.axhline(y=3)
plt.plot(pt3_x, pt3_y)
plt.grid(True)
plt.show()



