def a_func():
    """Выберем слова на латинице и запишем их с большой буквы"""

    for word in input("Введите буквы на латинице :\n").split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
        print(word.title() if chars == len(word) else f"{word} -  не все символы являются буквами латинского алфавита!")


print(a_func())
