with open('p5.2.txt','w', encoding="utf-8" ) as file:
    try:
        while True:
            user_text = input('Введите текст: ')
            file.write(user_text + '\n')
            if not user_text:
                break
        print(user_text, file=file)
    except FileNotFoundError:
    return 'Файл не найден.'