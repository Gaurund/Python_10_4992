'''
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.

4 4 -> 2 2
5 6 -> 2 3
'''


def input_integer(msg):
    num = input(msg)
    try:
        return (int(num))
    except ValueError:
        return input_integer("Необходимо ввести целое число. Повторите ввод: ")


def search_cross(sum, prod):
    for i in range(1001):
        for j in range(1001):
            if sum == i+j and prod == i*j:
                return (i, j)
    return "С заданными условиями решения нет."


def output():
    sum = input_integer("Чему равна сумма двух чисел? ")
    prod = input_integer("Чему равно их произведение? ")
    result = search_cross(sum, prod)
    print(sum, prod, "->", result)


output()
