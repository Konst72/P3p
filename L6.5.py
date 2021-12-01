class Stationery:

    def __init__(self, a, b ):
        self.title_1 = a
        self.color = b

    def drow(self):
        print(f"{self.title_1},{self.color}: Начинаем рисовать. ")


class Pen(Stationery):
    def drow(self):
        print(f"{self.title_1},{self.color}: Рисуем ручкой.")


class Pencil(Stationery):
    def drow(self):
        print(f"{self.title_1},{self.color}: Отрисовка карандашом.")


class Handle(Stationery):
    def drow(self):
        print(f"{self.title_1},{self.color}: Акцентируем маркером.")


pen = Pen("Ручка", "синяя")
pencil = Pencil("Карандаш", "графитовый")
handle = Handle("Маркер", "черный")

m_list_1 = [pen, pencil, handle]

for i in m_list_1:
    i.drow()
