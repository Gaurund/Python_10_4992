'''
Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
'''


def input_integer(msg):
    num = input(msg)
    try:
        return (int(num))
    except ValueError:
        return input_integer("Необходимо ввести именно число. Повторите ввод: ")


def get_coordinates():
    x = input_integer("Введите координату Х: ")
    y = input_integer("Введите координату Y: ")
    x_y = (x, y)
    return x_y


def output():
    coordinates = get_coordinates()
    if coordinates[0] > 0 and coordinates[1] > 0:
        print("Координаты в первой четверти.")
    elif coordinates[0] < 0 and coordinates[1] > 0:
        print("Координаты во второй четверти.")
    elif coordinates[0] < 0 and coordinates[1] < 0:
        print("Координаты в третьей четверти.")
    else:
        print("Координаты в четвертой четверти.")


output()
