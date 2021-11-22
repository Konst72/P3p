def my_list(**kwargs):
    return " ".join(kwargs.values())


print(my_list(Имя=input("Имя :"), инициалы=input("Инициалы :"),
              рожден=input("год рождения :"),
              телефон=input("телефон :"), email=input("email :")))
