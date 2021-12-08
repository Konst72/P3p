from abc import ABC, abstractmethod


class Clothes(ABC):
    resul = 0

    def __init__(self, par):
        self.par = par

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        Clothes.result += self.consumption + other.consumption
        return Suit(0)

    def __str__(self):
        rez = Clothes.result
        Clothes.result = 0
        return f"{res}"


class Coat(Clothes):
    @property
    def consumption(self):
        return round(self.par / 6.5) + 0.5


class Suit(Clothes):
    @property
    def consumption(self):
        return round(2 * self.par + 0.3)


coat = Coat(100)
suit = Suit(100)

print(coat.consumption)
print(suit.consumption)
print("Необходимо ткани для пошива : ",coat.consumption + suit.consumption, "метров.")
