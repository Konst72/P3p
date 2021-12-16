class ZeroErr(Exception):
    def __init__(self, intro):
        self.intro = intro


def division():
    try:
        num_1 = int(input("Введите делимое: "))
        num_2 = int(input("Введите делитель: "))
        if num_2 == 0:
            raise OwnError("Делить на ноль нельзя!")
        else:
            res = num_1 / num_2
            return f"Частное равно: {res}"
    except ValueError:
        return "Вы ввели не число"
    except ZeroErr as err:
        return err


print(division())