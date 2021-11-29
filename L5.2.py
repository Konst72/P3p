def count_info():
    try:
        with open('new_f.txt', 'r', encoding="utf-8") as text
            my_list = text.readlines()
            for index,value in enumerate(my_list,1):
                v_l = len(value.split())
                print(f'Количество слов построчно: {len(my_list)}. В {index + 1}-ой строке {len(v_l)} слов(а)')
    except FileNotFoundError:
        return 'Файл не найден.