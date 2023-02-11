'''
Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
2 2
4
'''


def input_integer(msg):
    num = input(msg)
    try:
        return (int(num))
    except ValueError:
        return input_integer("Необходимо ввести целое число. Повторите ввод: ")


def sum_a_b(a, b):
    if b == 1:
        return a+1
    return sum_a_b(a+1, b-1)


def output():
    a = input_integer("Введите первое слагаемое: ")
    b = input_integer("Введите второе слагаемое: ")
    result = sum_a_b(a, b)
    print("Сумма %d и %d равна %d" % (a, b, result))


output()
