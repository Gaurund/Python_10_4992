'''
Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''


def input_integer(msg):
    num = input(msg)
    try:
        return (int(num))
    except ValueError:
        return input_integer("Необходимо ввести целое число. Повторите ввод: ")


def a_to_b_power(a, b):
    if b <= 1:
        return a
    return a_to_b_power(a, b-1) * a


def output():
    a = input_integer("Какое число будем возводить в степень? ")
    b = input_integer("В какую степень будем возводить это число? ")
    result = a_to_b_power(a, b)
    print("Результат возведения числа %d в степень %d равен %d" % (a, b, result))


output()
