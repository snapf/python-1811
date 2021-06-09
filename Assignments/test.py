data_series = [-1, 2, -2, 3, 41, 38, 22, 10, -1, 3]
pattern = [40, 30, 20, 10]

# print(data_series[0]*pattern[0] + data_series[1]*pattern[1] + data_series[2]*pattern[2] + data_series[3]*pattern[3])

# print(data_series[1]*pattern[0] + data_series[2]*pattern[1] + data_series[3]*pattern[2] + data_series[4]*pattern[3])

similarity_list = []

for i in range(0, len(data_series) - 1):
    similarity_list.append(data_series[i]*pattern[i] + data_series[i + 1]*pattern[i + 1] + data_series[i + 2]*pattern[i + 2] + data_series[i+3]*pattern[i + 3])

print(similarity_list)
