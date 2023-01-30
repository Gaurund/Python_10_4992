'''
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет
'''


def input_integer(msg):
    num = input(msg)
    try:
        return (int(num))
    except ValueError:
        return input_integer("Необходимо ввести именно число. Повторите ввод: ")


def get_number():
    num = 0
    while not (0 < num < 8):
        num = input_integer("Введите номер дня недели: ")
        if not (0 < num < 8):
            print("Дни недели начинаются с 1 и заканчиваются 7. Повторите ввод.")
    return num


def output():
    num = get_number()
    if num > 5:
        print(num, "-> да")
    else:
        print(num, "-> нет")


output()
