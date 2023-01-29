'''
Задача 2: Найдите сумму цифр трехзначного числа. 

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)

'''


def input_integer(msg):
    num = input(msg)
    try:
        return (int(num))
    except ValueError:
        return input_integer("Необходимо ввести именно число. Повторите ввод: ")


def get_three_digits():
    num = 0
    while not (99 < num < 1000):
        num = input_integer("Пожалуйста, введите трёхзначное число: ")
        if not (99 < num < 1000):
            print("Число должно быть трёхзначным! Повторите ввод: ")
    return num


def summarize_digits(num):
    total = 0
    while num != 0:
        total = total + num % 10
        num = num // 10
    return total


def output():
    num = get_three_digits()
    total = summarize_digits(num)
    print(num, "->", total)


output()
