my_list=[5,4,3,2,1]
new_number =int(input("Ведите натуральное число:"))
i=0
for n in my_list:
    if new_number <= n:
        i +=1
    else:
        break
my_list. insert(i, new_number)
print(my_list)