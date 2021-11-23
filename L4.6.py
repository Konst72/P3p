from itertools import count, cycle

iterator = count(int(input('Введите целое число :')))
print('Список из четырнадцати чисел после введённого числа: ')
for i in range(14):
   print(next(iterator), end=' ')

"""Второй блок для повтора заданного списка трижды """

print('\n- повтор  -')
my_l = ['те же самые)', 101, 3.1415, 15.457]
iterator = cycle(my_l)
for i in range(len(my_l) * 3):
   print(next(iterator), end=' ')
