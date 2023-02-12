'''
Задача №37. Решение в группах
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
'''


def rev_line(limit):
    if limit == 0:
        return
    num = int(input())
    rev_line(limit - 1)
    print(num, end=' ')


rev_line(int(input('Введите количество элементов: ')))
