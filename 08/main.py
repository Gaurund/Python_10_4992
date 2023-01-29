'''
Задача 8: Требуется определить, можно ли от шоколадки размером n
× m долек отломить k долек, если разрешается сделать один разлом по
прямой между дольками (то есть разломить шоколадку на два
прямоугольника).

3 2 4 -> yes
3 2 1 -> no

'''


def input_integer(msg):
    num = input(msg)
    try:
        return (int(num))
    except ValueError:
        return input_integer("Необходимо ввести целое число. Повторите ввод: ")


def output():
    print("Введите размер шоколадной плитки в дольках")
    width = input_integer("Сколько долек по одной стороне? ")
    length = input_integer("А сколько долек по другой? ")
    cut = input_integer("Сколько долек вы хотите отломить? ")
    if width*length > cut:
        if cut % width == 0 or cut % length == 0:
            print("Это можно.")
        else:
            print("За один раз не получится.")
    elif width*length == cut:
        print("Так это вся шоколадка. Берите целиком!")
    else:
        print("Шоколадка меньше чем кусок, который вы хотите отломить. Не жадничайте!")


output()
