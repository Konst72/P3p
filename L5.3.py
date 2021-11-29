with open(('p5.3.txt','w', encoding="utf-8" ) as file)
    selection = {line.split()[0]: float(line.split()[1]) for line in file}
    print(f"Средняя зарплата = {round((sum(selection.values()) / len(selection),2))}\n"
       f"Зарплату менее 20 тыс.руб имеют {[el[0] for el in selection.items() if el[1]<20000]}")
    