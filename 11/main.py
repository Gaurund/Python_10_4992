'''
Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

Input: 5

Output: 6'''


def input_integer(msg):
    num = input(msg)
    try:
        return (int(num))
    except ValueError:
        return input_integer("Необходимо ввести целое число. Повторите ввод: ")


def get_number():
    num = input_integer("Введите целое неотрицательное число: ")
    while num < 0:
        num = input_integer(
            "Пожалуйста, введите неотрицательное число. Повторите ввод: ")
    return num


def fibonacci(num):
    if num == 0:
        return 1
    f1 = 0
    f2 = 1
    count = 2
    while num > f2:
        count += 1
        f1, f2 = f2, f1+f2
    if num == f2:
        return count
    return -1


def output():
    num = get_number()
    fib = fibonacci(num)
    print(fib)


output()
