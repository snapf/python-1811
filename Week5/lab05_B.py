
# Experimental data
datasets = []
datasets.append([14.2, 32.5, 42.1, 74.5, 43.5])
datasets.append([25.7, 34.1, 48.7, 50.3])
datasets.append([11.2, 26.9, 95.1, 52.1, 23.5, 5.6, 45.7, 37.8])
datasets.append([54.7, 25.3])
datasets.append([-24.7, -57.3, -145.5])
datasets.append([-12.5, 14.5, -452, -734.4])


summary_list = []

for i in range(0,len(datasets)):
    summary_list.append(max(datasets[i]) / len(datasets[i]))

print(summary_list)


# For checking, the expected answers are:
# [2.84, 6.425, 0.7, 12.65]


