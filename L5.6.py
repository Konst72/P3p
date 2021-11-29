def title():
    try:
        m_dict = {}
        with open("file.txt", encoding='utf-8') as fobj:
            for line in fobj:
                name, stats = line.split(':')
                name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()))
                m_dict[name] = name_sum
            print(f"{m_dict}")  # вывод:{'Математический анализ': 170}
    except FileNotFoundError:
        return 'Файл не найден.'


title()