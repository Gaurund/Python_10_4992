'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.

11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12
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


def fill_list(size, msg):
    print(msg)
    new_list = []
    for i in range(size):
        new_list.append(input_integer(f'Введите {i+1} число списка: '))
    return new_list


def output():
    first_set_size = get_number("Введите размер первого набора чисел: ",
                                "Число не может быть отрицательным!")
    second_set_size = get_number("Введите размер второго набора чисел: ",
                                 "Число не может быть отрицательным!")
    first_list = fill_list(first_set_size, 'Заполните первый набор чисел.')
    second_list = fill_list(second_set_size, 'Заполните второй набор чисел.')

    first_set = set(first_list)
    second_set = set(second_list)

    set_intersection = first_set.intersection(second_set)
    list_intersection = list(set_intersection)
    list_intersection.sort()

    print('В наборах чисел', first_list, 'и',
          second_list, 'встречаются следующие числа:')
    print(*list_intersection, sep=', ')


output()
