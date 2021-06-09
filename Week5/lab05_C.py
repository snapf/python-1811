
import matplotlib.pyplot as plt

# create a list of time instants
with open('time_data_complete.txt') as f:
    time_str_list = f.read().splitlines()

# load file the contains the voltage measurements
# create a list of voltage values
with open('voltage_data_complete.txt') as f:
    voltage_str_list = f.read().splitlines()

# convert to elements in the list to float data type
time_list = [float(t) for t in time_str_list]
voltage_list = [float(v) for v in voltage_str_list]

# Plot a graph of the data
fig1 = plt.figure()         # create a new figure
plt.plot(time_list,voltage_list, '--x')
plt.xlabel('time [s]')    # label for x-axis
plt.ylabel('voltage [V]')   # label for y-axis
plt.axhline(y=3, color='r', linestyle=':')
plt.title('Pulse oximeter data')  # title of the graph
plt.grid()  # display the grid
plt.show()  # to display the graph


########### PUT YOUR SOLUTION BELOW ###########
peak_list = []

threshold = 3

for i in range(0, len(voltage_list) - 1):
    if voltage_list[i] < threshold and voltage_list[i + 1] > threshold:
        peak_list.append(i)

print(f"Total number of peaks is: {len(peak_list)}")
