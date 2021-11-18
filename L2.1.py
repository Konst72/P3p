my_list = [5, 'name', complex(10, 11), [3, 4], {2, 6}, (7, 'a'),
           {'k': 8, 't': 9}]
print(my_list)
for i, v in enumerate(my_list, 1):
    print(f"{i}, {v} - {type(v)}")
