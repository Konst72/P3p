def fakt_start(numb):
    fun_num = 1
    """Нарастающий итог"""

    for i in range(numb + 1):
        yield f'{i}!= {fun_num}'
        fun_num *= i + 1


for el in fakt_start(int(input("Фактериал какого числа необходимо вычислить?- "))):
    print(el)
