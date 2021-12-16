class OffEq:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.items = {'Добавлено устройство': self.name, 'Модель': name, 'Цена за ед': self.price,
                      'Количество': self.quantity}

    def income(self):
        name = input("Наименование:")
        price = int(input(f'Цена за ед: '))
        quantity = int(input(f'Количество: '))
        item = {'Модель': name, 'Цена за ед': price, 'Количество': quantity}
        self.items.update(item)
        print(self.items)



class Printer(OffEq):
    def income(self):
        try:
            if k == "a":
                name = input('Модель принт : ')
                price = int(input(f'Цена за ед: '))
                quantity = int(input(f'Количество: '))
                item = {'Модель': name, 'Цена за ед': price, 'Количество': quantity}
                self.items.update(item)
                print(self.items)

            else:
                return f'Может, вы хотите добавить сканер?'
            exit()
        except ValueError:
            print('Недопустимое значение!')

class Scanner(OffEq):

    def income(self):
        if k == "b":
            name = input('Модель сканkра : ')
            price = int(input(f'Цена за ед: '))
            quantity = int(input(f'Количество: '))
            item = {'Модель': name, 'Цена за ед': price, 'Количество': quantity}
            self.items.update(item)
            print(self.items)
        else:
            return f'Тогда Добавить ксерокс'
        exit()

class Xerox(OffEq):

    def income(self):
        if k == "c":
            name = input('Модель ксерокса : ')
            price = int(input(f'Цена за ед: '))
            quantity = int(input(f'Количество: '))
            item = {'Модель': name, 'Цена за ед': price, 'Количество': quantity}
            self.items.update(item)
            print(self.items)
        else:
            return f'Увы,Нет такой категории'
        exit()

k = input("Введите категорию(a- принтер,b- сканер,c- ксерокс):")

p = Printer('Принтjр', 0, 0)
s = Scanner('Сканор', 0, 0)
x = Xerox('Ксерbкс', 0, 0)

p.income()
s.income()
x.income()


