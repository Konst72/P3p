import statement
profit = {}
pr  = {}
prof = 0
prof_aver = 0
i = 0
with open('l5.7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Средняя прибыль - {prof_aver:.2f}')
    else:
        print(f'Прибыль отсутсвует. Убыток корпорации')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждого  филиала - {profit}')

with open('file_7.json', 'w') as write_js:
    statement.dump(profit, write_js)

    js_str = statement.dumps(profit)
    print(f'Создан файл с расширением json с данными: \n '
          f' {js_str}')