'''
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
'''
import math


def input_integer(msg):
    num = input(msg)
    try:
        return (int(num))
    except ValueError:
        return input_integer("Необходимо ввести именно число. Повторите ввод: ")


def get_coordinates(msg):
    print(msg)
    x = input_integer("Введите координату Х: ")
    y = input_integer("Введите координату Y: ")
    x_y = (x, y)
    return x_y


def count_distance(first_point, second_point):
    result = math.sqrt(abs((second_point[0]-first_point[0])**2 +
                       (second_point[1]-first_point[1])**2))
    return result


def output():
    first_point = get_coordinates("Введите координаты первой точки")
    second_point = get_coordinates("Введите координаты второй точки")
    result = count_distance(first_point, second_point)
    print("А {}; B {} -> {}".format(first_point, second_point, round(result, 2)))


output()
