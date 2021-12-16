class MyErr(Exception):
    def __init__(self):
        pass


class CheckText:
    def __init__(self):
        self.my_l = []

    def enter_dat(self):
        global from_us
        while True:
            try:
                try:
                    from_us = int(input('Введите числа: '))
                    exits = input(f"Число {from_us} в списке. Если хотите завершить, наберите 'stop'.").lower()
                    self.my_l.append(from_us)
                    if exits == 'stop':
                        print(self.my_l)
                        break
                except ValueError:
                    raise MyErr
            except MyErr:
                exits = input(f"Вы ввели не число! если хотите закончить, наберите команду 'stop'").lower()
                if exits == 'stop':
                    print(self.my_l)
                    break
                else:
                    self.enter_dat()


a = CheckText()
a.enter_dat()
