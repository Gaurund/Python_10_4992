'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
5 -> 1 0 1 1 0
2
'''
import random


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


def create_random_list(size, low, high):
    random_list = []
    for i in range(size):
        random_list.append(random.randint(low, high))
    return random_list


def count_head_tails(coins_list):
    size = len(coins_list)
    count = 0
    for i in range(size):
        if coins_list[i] == 0:
            count += 1
    if size // 2 < count:
        count = size - count
    return count


def output():
    coins = get_number("Введите количество монеток: ", "Число не может быть отрицательным!")
    HEAD = 0
    TAIL = 1
    coins_list = create_random_list(coins, HEAD, TAIL)
    flips = count_head_tails(coins_list)
    print("%d монет -> " % coins, *coins_list)
    print("Потребуется %d переворота(ов)." % flips)


output()
