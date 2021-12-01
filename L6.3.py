class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"доход": wage, "премия": bonus}


class Position(Worker):
    def get_ful_name(self):
        return f"{self.name}{self.surname}"

    def get_ful_profit(self):
        return f"{sum(self._income.values())}"


info = Position("Иванов ", "Петр ", "Менеджер по продажам ", 150000, 50000)
print(info.get_ful_name())
print(info.get_ful_profit())
print(info.position)









