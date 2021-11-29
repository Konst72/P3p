r_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("l5.4.txt", "w", encoding="utf-8") as n_f:
    with open("l5.4a.txt", "w", encoding="utf-8") as my_f:
        n_f.writelines([line.replace(line.split()[0], r_dict.get(line.split()[0])) for line in my_f])
       