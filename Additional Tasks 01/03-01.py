'''
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''
import random


def create_randomized_list(size, low, high):
    rand_list = [random.randint(low, high) for _ in range(size)]
    return rand_list


def input_integer(msg):
    num = input(msg)
    try:
        return (int(num))
    except ValueError:
        return input_integer("Необходимо ввести целое число. Повторите ввод: ")


def search_odd(list_):
    odd_list = list_[1::2]
    return odd_list


def output():
    size = input_integer('Введите размер списка: ')
    low = input_integer('Введите наименьшее значение в спике: ')
    high = input_integer('Введите наибольшее значение в спике: ')
    rnd_int_list = create_randomized_list(size, low, high)
    odd_list = search_odd(rnd_int_list)
    print("В массиве [", end=' ')
    print(*rnd_int_list, sep=', ', end=" ] ")
    print('сумма на нечётных позициях равна: ', sum(odd_list))


output()
