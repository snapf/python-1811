import matplotlib.pyplot as plt


data_values = [-1, 5, 4, 8, 3, 21, 18, 16, 3, 2, 3, 1, 4, 5, 17, 22, 36, 33, 34, 9, 1, -2]
data_values = data_values + [-2, 4, -1, 7, 13, 12, 3, 1, 4, 5, 26, 22, 28, 27, 26, 2, 8, 6]

# x_list = [ i for i in range(0,len(data_values))]

# plt.bar(x_list, data_values)
# # plt.plot(x_list, threshold_list, 'r' )
# plt.grid(True)
# plt.show()

pattern_width = 4
threshold = 15
peak = []
for i in range(1,len(data_values)-1):
    if data_values[i-1] <= data_values[i] and data_values[i+1] <= data_values[i+1] and data_values[i] >= threshold:
        peak.append(data_values[i])

data_sliced = []
for k in range(len(peak)):
    data_sliced.append(peak[slice(k, k + pattern_width)])

for j in range(len(data_sliced))
# peak2 = []
# for j in range(len(data_sliced)):
#     if len(data_sliced[j]) == pattern_width:
#         for g in range(1,len(data_sliced[j]) - 1):
#             if data_sliced[g-1] <= data_sliced[g] and data_sliced[g+1] <= data_sliced[g]:
#                 peak2.append(data_sliced[j][g])

# print(peak2)
# print(index)

# [21, 17, 22, 36, 34, 26, 28]
# expected_answer = [5, 16, 26, 34]


# peak2 = []
# for j in range(1,len(peak)-1):
#     if peak[j-1] <= peak[j] and peak[j+1] <= peak[j]:
#         # peak2.append(peak[j])
#         peak2.append(data_values.index(peak[j]))
# peak2.append(peak[0])
# peak2.append(peak[-1])

# index = []
# for k in range(len(peak2)):
#     index.append(data_values.index(peak2[k]))