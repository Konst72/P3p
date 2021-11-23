from random import randint

start_list = [randint(-20, 20) for _ in range(25)]
new_list = [el for el in start_list if start_list.count(el) == 1]
print(f"список\n{start_list}\nбез повторений\n{new_list}")