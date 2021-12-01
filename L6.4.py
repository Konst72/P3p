from random import choice
class Car:
    movement = ['вперёд', 'назад', 'направо', 'налево']

    def __init__(self, a, b, c, p=False):
        self.name = a  # название
        self.color = b  # цвет
        self.speed = c  # скорость
        self.is_police = p
        print(f"Новая машина: {a} цвет: {b}.\nЭто полицейская машина? {p}")

    def go(self):
        print(f"{self.name}: Машина поехала.")

    def stoping(self):
        print(f"{self.name}: Машина остановилась.")

    def turn(self):
        print(f"{self.name}: машина повернула {choice(self.movement)}.")

    def show_speed(self):
        return f"{self.name}: Скорость машины {self.speed}."


class FavoriteCar(Car):

    def show_speed(self):
        return f"{self.name}: Скорость машины {self.speed}. Превышение !" if self.speed > 60 else super().show_speed()


class Truck(Car):

    def show_speed(self):
        return f"{self.name}: Скорость машины {self.speed}. Превышение !" if self.speed > 40 else super().show_speed()


class Sport(Car):
    def show_speed(self):
        return f"{self.name}: Скорость машины {self.speed}. Превышение !" if self.speed > 100 else super().show_speed()


class Polise(Car):
    def __init__(self, a, b, c, p=True):
        super().__init__(a, b, c, p=True)


polise = Polise("Уаз", "серый", 60)
favorite_car = FavoriteCar("Lexus", "Белый", 80)
truck = Truck("Kamaz", "Оранжевый", 30)
sport = Sport("Lamborghini", "красная", 120)


l_cars = [favorite_car, truck, sport, polise]

for i in l_cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stoping()
    print()



