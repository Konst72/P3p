with open('l5.5.txt', 'w', encoding="utf-8") as m_file:
    m_file = [randint(1, 1000) for _ in range(10000)]
    file.write(" ".join(map(str, m_file)))

print(f" Сумма элементов - {sum(m_file)}")
