num_list = [1.5, 2.4, 6.5]
cumulative_sum_list = []

k = 0
for i in range(0,len(num_list)):
    k += num_list[i]
    cumulative_sum_list.append(k)

print(cumulative_sum_list)
