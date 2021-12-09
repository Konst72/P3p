
class CompN:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма "c_1" и "c_2" равна: ({self.a + other.a}+{self.b + other.b}i)'

    def __mul__(self, other):
        return f'Произведение "c_1" и "c_2"  равно: ({self.a * other.a - (self.b * other.b)}+{self.b * other.a}i)'


c_1 = CompN(int(input("Введите число 1: ")),int(input("введите число 2: ")))
c_2 = CompN(int(input("Введите коэффициент 1: ")),int(input("введите коэффициент 2: ")))

print(c_1 + c_2)
print(c_1 * c_2)

