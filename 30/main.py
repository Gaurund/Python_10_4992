'''
Задача 30: Заполните массив элементами арифметической
прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15
'''


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


def print_progression(start, step, steps):
    end = start + steps * step
    for i in range(start, end, step):
        print(i, end=" ")


def output():
    ERROR_MSG = "По условию число должно быть положительным. "
    start = int(get_number("Введите начало прогрессии: ", ERROR_MSG))
    step = int(get_number("Введите шаг прогрессии: ", ERROR_MSG))
    steps = int(get_number(
        "Введите сколько шагов прогрессии вы хотите увидеть: ", ERROR_MSG))
    print_progression(start, step, steps)


output()
