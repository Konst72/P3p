from sys import argv

def zarp():
    try:
        day, price, bonus = map(int, argv[1:])
        print(f"Заработная плата равна {day * price + bonus}")
    except ValueError:
        print(" Необходимы все три характеристики !")

zarp()