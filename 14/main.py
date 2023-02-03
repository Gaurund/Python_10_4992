'''
Задача 14: Требуется вывести все целые степени двойки (т.е. числа
вида 2**k), не превосходящие числа N.

10 -> 1 2 4 8

'''
import math


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


def create_power_of_two_list(num):
    size = math.floor(math.log(num, 2))
    return [2**i for i in range(size+1)]


def output():
    num = get_number("Введите целое неотрицательное число: ",
                     "Число не может быть отрицательным!")
    power_of_two_list = create_power_of_two_list(num)
    print(num, "->", *power_of_two_list)


output()
