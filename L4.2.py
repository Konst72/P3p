list_start = [11, 56,2,14,178,8,3]
n_list = [list_start[i] for i in range(1, len(list_start)) if list_start[i] > list_start[i - 1]]
print(n_list)