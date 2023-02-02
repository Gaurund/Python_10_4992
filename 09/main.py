'''
По данному целому неотрицательному n вычислите значение n!. 
N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
Решить задачу используя цикл while

Input: 5

Output: 120
'''


def input_integer(msg):
    num = input(msg)
    try:
        return (int(num))
    except ValueError:
        return input_integer("Необходимо ввести целое число. Повторите ввод: ")


def get_number():
    num = input_integer("Введите целое неотрицательное число: ")
    while num < 0:
        print("Число не может быть отрицательным!")
        num = input_integer("Введите целое неотрицательное число: ")
    return num


def factorial(num):
    fac = 1
    while num != 0:
        fac *= num
        num -= 1
    return fac


def output():
    num = get_number()
    fac = factorial(num)
    print("Факториал числа %d равен %d" % (num, fac))


output()
