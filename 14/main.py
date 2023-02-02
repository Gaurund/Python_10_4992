'''
Задача 14: Требуется вывести все целые степени двойки (т.е. числа
вида 2**k), не превосходящие числа N.

10 -> 1 2 4 8

'''


def input_integer(msg):
    num = input(msg)
    try:
        return (int(num))
    except ValueError:
        return input_integer("Необходимо ввести целое число. Повторите ввод: ")


def get_number():
    num = input_integer("Введите целое неотрицательное число: ")
    while num < 1:
        print("Число не может быть отрицательным!")
        num = input_integer("Введите целое неотрицательное число: ")
    return num


def create_list_power_of_two(num):
    power = 0
    TWO = 2
    power_of_two_list = []
    while num > TWO**power:
        power_of_two_list.append(TWO**power)
        power += 1
    return power_of_two_list


def output():
    num = get_number()
    power_of_two_list = create_list_power_of_two(num)
    print(num,"->",*power_of_two_list)


output()
