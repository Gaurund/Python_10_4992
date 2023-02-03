'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai
. Последняя строка
содержит число X
5
1 2 3 4 5
6
-> 5
'''

import random


def input_integer(msg):
    num = input(msg)
    try:
        return (int(num))
    except ValueError:
        return input_integer("Необходимо ввести целое число. Повторите ввод: ")


def get_number(invite_msg, error_msg):
    num = input_integer(invite_msg)
    while num < 1:
        print(error_msg)
        num = input_integer(invite_msg)
    return num


def search_nearest(new_list, value):
    nearest = new_list[0]
    for i in new_list:
        if abs(value - nearest) > abs(value - i):
            nearest = i
    return nearest


def output():
    size = get_number("Введите размер списка: ",
                      "Число не может быть отрицательным!")
    low = input_integer("Введите нижний предел значений элементов списка: ")
    high = input_integer("Введите верхний предел значений элементов списка: ")
    new_list = [(random.randint(low, high)) for _ in range(size)]
    print(new_list)
    value = input_integer("К какому числу ищем приближение? ")
    nearest = search_nearest(new_list, value)
    print("->", nearest)


output()
