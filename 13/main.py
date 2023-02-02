'''
Уставшие от необычно теплой зимы, жители решили узнать,
действительно ли это самая длинная оттепель за всю историю
наблюдений за погодой. Они обратились к синоптикам, а те, в
свою очередь, занялись исследованиями статистики за
прошлые годы. Их интересует, сколько дней длилась самая
длинная оттепель. Оттепелью они называют период, в
который среднесуточная температура ежедневно превышала
0 градусов Цельсия. Напишите программу, помогающую
синоптикам в работе.
Пользователь вводит число N – общее количество
рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
располагается N целых чисел.
Каждое число – среднесуточная температура в
соответствующий день. Температуры – целые числа и лежат в
диапазоне от –50 до 50
Input: 6 -> -20 30 -40 50 10 -10
Output: 2
'''


def input_integer(msg):
    num = input(msg)
    try:
        return (int(num))
    except ValueError:
        return input_integer("Необходимо ввести целое число. Повторите ввод: ")


def get_number():
    num = input_integer("Введите целое неотрицательное число: ")
    while num < 1:
        num = input_integer(
            "Пожалуйста, введите неотрицательное число. Повторите ввод: ")
    return num


def input_temperature(days):
    total_days_list = []
    for i in range(days):
        total_days_list.append(input_integer("Температура %d дня: " % (i+1)))
    return total_days_list


def warm_days(total_days_list):
    count = 0
    warm_days_list = [count]
    for i in range(len(total_days_list)):
        if total_days_list[i] > 0:
            warm_days_list[count] += 1
        elif total_days_list[i] <= 0 and warm_days_list[count] != 0:
            count += 1
            warm_days_list.append(0)
    warm_days_list.sort()
    return warm_days_list[count]


def output():
    days = get_number()
    total_days_list = input_temperature(days)
    warm_days_total = warm_days(total_days_list)
    print("Оттепель была %d дней" % warm_days_total)
    # print(*total_days_list)


output()
