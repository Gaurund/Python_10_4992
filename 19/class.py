'''
Задача №19. Решение в группах
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
'''

from random import randint

n = int(input('Введите длину списка: '))
my_list = [randint(1, 100) for i in range(n)]
print(my_list)

k = int(input('Сдвиг: '))
for i in range(k):
    my_list.insert(0, my_list[n-1])
    my_list.pop(n)
print(my_list)


