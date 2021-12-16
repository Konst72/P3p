class OffEq:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.items = {'Добавлено устройство': self.name, 'Модель': name, 'Цена за ед': self.price,
                      'Количество': self.quantity}

    def income(self):
        try:

            name = input(f'Модель:')
            price = int(input(f'Цена за ед: '))
            quantity = int(input(f'Количество: '))
            item = {'Модель': name, 'Цена за ед': price, 'Количество': quantity}
            self.items.update(item)
            print(self.items)
        except ValueError:
            print('Недопустимое значение!')


class Printer(OffEq):
    def income(self):
        super().income()

class Scanner(OffEq):
    def income(self):
        super().income()

class Xerox(OffEq):
    def income(self):
        super().income()


p = Printer('Принтjр', 0, 0)
s = Scanner('Сканор', 0, 0)
x = Xerox('Ксерbкс', 0, 0)

p.income()
s.income()
x.income()

