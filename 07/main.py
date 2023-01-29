'''
Задача №7. Решение в группах
Дано натуральное число. Требуется определить,
является ли год с данным номером високосным. Если
год является високосным, то выведите YES, иначе
выведите NO. Напомним, что в соответствии с
григорианским календарем, год является
високосным, если его номер кратен 4, но не кратен
100, а также если он кратен 400.
Input: 2016
Output: YES
'''


def input_integer(msg):
    return int(input(msg))


def leap_year():
    year = input_integer("Please input a year: ")
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Yes, it is a leap year!")
    else:
        print("Nope, it isn't.")


leap_year()
