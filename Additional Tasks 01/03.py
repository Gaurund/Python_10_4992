'''
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

'''


def input_integer(msg):
    num = input(msg)
    try:
        return (int(num))
    except ValueError:
        return input_integer("Необходимо ввести именно число. Повторите ввод: ")


def get_quarter():
    num = 0
    while not (0 < num < 5):
        num = input_integer("Введите номер четверти: ")
        if not (0 < num < 5):
            print("Число должно быть от 1 до 4 включительно.")
    return num


def output():
    num = get_quarter()
    coordinates = ("x > 0 и y > 0", "x < 0 и y > 0",
                   "x < 0 и y < 0", "x > 0 и y < 0")
    print(coordinates[num-1])


output()
