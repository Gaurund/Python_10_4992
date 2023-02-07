"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел A i
. Последняя строка
содержит число X
5
1 2 3 4 5
6
-> 5
"""
x = 6


my_list = [10, 15, 25, 37, 122, 5, 7, 0, 88, 17]
print(my_list)
my_list.append(x)
list.sort(my_list)
if x == my_list[0]:
    print(my_list[1])
elif x == my_list[-1]:
    print(my_list[-2])
else:
    b = my_list.index(x)
    b0 = b - 1
    b1 = b + 1
    if x-my_list[b0] < my_list[b1]-x:
        print(my_list[b0])
    elif x-my_list[b0] > my_list[b1]-x:
        print(my_list[b1])
    else:
        print(my_list[b0])
        print(my_list[b1])
    

