'''
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
'''

from random import randint

# my_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

my_list = [randint(-20, 20) for _ in range(20)]
print(my_list)
count_list = []
low_limit = 1
high_limit = 10
for i in range(len(my_list)):
    if low_limit <= my_list[i] <= high_limit:
        count_list.append(i)

print(count_list)
