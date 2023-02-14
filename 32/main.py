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


def create_random_array(size, min, max):
    return [(random.randint(min, max)) for _ in range(size)]


def count_in_range(array, low_limit, high_limit):
    count_list = []
    for i in range(len(array)):
        if low_limit <= array[i] <= high_limit:
            count_list.append(i)
    return count_list


def output():
    array_size = get_number("Введите размер массива: ",
                            "Побойтесь Бога! Размер не может быть таким. Повторите ввод: ")
    min_array_value = input_integer(
        "Введите минимальное возможное значение в массиве: ")
    max_array_value = input_integer(
        "Введите максимальное возможное значение в массиве: ")
    low_limit = input_integer("Введите нижний порог диапазона: ")
    high_limit = input_integer("Введите верхний порог диапазона: ")

    array = create_random_array(array_size, min_array_value, max_array_value)
    print(array)

    counted = count_in_range(array, low_limit, high_limit)
    print(counted)


output()
