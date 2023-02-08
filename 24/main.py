'''
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai
 ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.

4 -> 1 2 3 4
9
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


def fill_berries_list(size, msg):
    print(msg)
    new_list = []
    for i in range(1, size+1):
        new_list.append(input_integer(f'{i} куст: '))
    return new_list


def count_best_bushes(berries):
    size = len(berries)
    max_berries = sum(berries[:3])
    berries = berries + berries[:1]
    for i in range(1, size):
        if max_berries < sum(berries[i:i+3]):
            max_berries = sum(berries[i:i+3])
    return max_berries


def output():
    bushes = get_number("Введите количество кустов: ",
                        "Число не может быть отрицательным!")
    berries_on_bushes = fill_berries_list(
        bushes, 'Сколько ягод на каждом кусте?')
    best_bushes = count_best_bushes(berries_on_bushes)
    print('Максимальное число ягод с кустов:', best_bushes)


output()
