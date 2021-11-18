my_list = input("введите несколько слов с пробелами : ").split()
for i, word in enumerate(my_list, 1):
    print(f"{i}. {word[:10]}")
