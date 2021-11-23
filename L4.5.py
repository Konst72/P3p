from functools import reduce

def m_list(s_1, s_2):
    return s_1 * s_2

new_list = [el for el in range(100, 1001, 2)]
print(f"\a\a\a\a\nСписок \n{new_list}\n\a\a\a\a\nПроизведение всех элементов\n{reduce(m_list,new_list)}\n\a\a\a\a")

