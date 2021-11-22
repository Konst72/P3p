def my_fun(s_1, s_2):
    try:
        s_1 = int(s_1)
        s_2 = int(s_2)
        diff = s_1 / s_2
    except ValueError as error:
        print("Error")
        return "Не является числом"
    except ZeroDivisionError as error:
        print("Error")
        return "На ноль делить нельзя"
    return round(diff, 3)


print("Результат деления:",{my_fun(input("Введите первое число :"),
                                   input("Введите второе число :"))})

