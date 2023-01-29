'''Задача №3. Решение в группах
В некоторой школе решили набрать три новых
математических класса и оборудовать кабинеты для
них новыми партами. За каждой партой может сидеть
два учащихся. Известно количество учащихся в
каждом из трех классов. Выведите наименьшее
число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32'''

import math

def input_number(num):
    return int(input("Введите количество учеников в %d классе: " % (num+1)))

def count_desks(classes):
    total = 0
    for e in range(classes):
        total += input_number(e)
    return math.ceil(total/2)

print(count_desks(3))

# def count_desks(cls):
#     total = 0
#     for e in cls:
#         total += e
#     return math.ceil(total/2)

# classes = []
# for e in range(3):
#     classes.append(input_number(e))

# print(count_desks(classes))