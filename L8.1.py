from datetime import date


class Data:
    def __init__(self, data):
        self.data = data.split('-')

    @classmethod
    def type(cls, data):
        try:
            day, month, year = [int(i) for i in data.split('-')]
            return f"{type(day), day}{type(month), month}{type(year), year}"
        except ValueError:
            return 'Не существует такой даты!'

    @staticmethod
    def check(data):
        try:
            d, m, y = data.split('-')
            date(int(y), int(m), int(d))
            return 'Есть такая дата ,'
        except ValueError:
            return 'Указана неправильная дата!'


data = (input("Введите дату через дефис: "))

print((Data.check(data)),"вы ввели", data)
print(Data.type(data))