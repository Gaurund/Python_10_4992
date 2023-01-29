'''
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
программу, которая проверяет счастливость билета.

385916 -> yes
123456 -> no
'''


def input_integer(msg):
    num = input(msg)
    try:
        return (int(num))
    except ValueError:
        return input_integer("Необходимо ввести целое шестизначное число. Повторите ввод: ")


def get_six_digits():
    num = 0
    while not (99999 < num < 1000000):
        num = input_integer("Пожалуйста, введите шестизначное число: ")
        if not (99999 < num < 1000000):
            print("Число должно быть шестизначным! Повторите ввод: ")
    return num


def summarize_digits(num):
    total = 0
    while num != 0:
        total = total + num % 10
        num = num // 10
    return total


def output():
    ticket = get_six_digits()
    first_half = ticket // 1000
    second_half = ticket - first_half*1000
    first_half_sum = summarize_digits(first_half)
    second_half_sum = summarize_digits(second_half)
    if first_half_sum == second_half_sum:
        print("%d -> Да" % (ticket))
    else:
        print("%d -> Нет" % (ticket))


output()
