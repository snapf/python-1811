import numpy as np
import matplotlib.pyplot as plt

data_sea_ice = np.loadtxt(fname="sea_ice.txt")

# print("The shape of the numpy array is: ", data_sea_ice.shape)

# print("The first row of data is \n", data_sea_ice[0,:])

years = data_sea_ice[:,0];
data_sea_ice = np.delete(data_sea_ice, 0, axis=1)
# print("The shape of the numpy array is: ", data_sea_ice.shape)

months = np.linspace(0.5,12,24)

plt.figure(1)
plt.plot(months, np.transpose(data_sea_ice))
plt.xticks([2, 4, 6, 8, 10, 12], ["Feb", "Apr", "Jun", "Aug", "Oct", "Dec"])
# plt.show()


# ! Task 1
# avg_sea_ice_annual = np.average(data_sea_ice, axis = 1)
avg_sea_ice_annual = data_sea_ice.mean(axis = 1)
print(f"Average sea ice annually is\n{avg_sea_ice_annual}\n")

# ! Task 2
# avg_sea_ice_half_month = np.average(data_sea_ice, axis = 0)
avg_sea_ice_half_month = data_sea_ice.mean(axis = 0)
print(f"Average sea ice half month is\n{avg_sea_ice_half_month}\n")

# ! Task 3
avg_sea_ice = np.mean(data_sea_ice)
print("3\n",avg_sea_ice)
print(f"Average sea ice total is\n{avg_sea_ice}\n")

# ! Task 4
h_m_exceeds = np.sum(data_sea_ice > avg_sea_ice, axis = 1)
print(f"avg exceeds half month\n{h_m_exceeds}\n")

# ! Task 5
less_than_avg = np.sum(avg_sea_ice_annual < avg_sea_ice, axis = 0)
print(f"avg less than\n{less_than_avg}\n")

# ! Task 6
last_decade = avg_sea_ice_annual[-10:]
last_decade_less_than_avg = np.sum(last_decade < avg_sea_ice)
print(f"last decade less than average\n{last_decade_less_than_avg}\n")

# ! Task 7
increasing = np.argsort(avg_sea_ice_annual)
ordered = increasing[:10]
last = years[ordered]
print(last)

# ! task 8
sea_ice_mflat = np.reshape(data_sea_ice, (420,2))
average_monthly = np.mean(sea_ice_mflat, axis = 1)
final = np.reshape(average_monthly, (35,12))
print(final)



