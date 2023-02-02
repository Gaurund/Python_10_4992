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


def get_number(invite_msg, error_msg):
    num = input_integer(invite_msg)
    while num < 1:
        print(error_msg)
        num = input_integer(invite_msg)
    return num

def search_cross(sum, prod):
    for i in range(1001):
        for j in range(1001):
            if sum == i+j and prod == i*j:
                return (i, j)
    return "С заданными условиями решения нет."


def output():
    sum = get_number("Чему равна сумма двух чисел? ", "По условию число должно быть положительным. ")
    prod = get_number("Чему равно их произведение? ", "По условию число должно быть положительным. ")
    result = search_cross(sum, prod)
    print(sum, prod, "->", result)


output()
