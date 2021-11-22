def sum_num():
    s = 0
    """Рассчитаем сумму чисел с нарастающим итогом"""

    while True:
        m_l = input("Введите числа с пробелами, или z для выхода: ").split()
        for num in m_l:
            if num.lower() == "z":
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    print("Вы ввели не числа. Введите корректное значение или нажмите z для выхода")
        print(f"Сумма с нарастающим итогом = {s}")


print(sum_num())
