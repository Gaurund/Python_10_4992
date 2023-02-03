'''
Задача №17. Решение в группах
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
'''


def input_integer(msg):
    num = input(msg)
    try:
        return (int(num))
    except ValueError:
        return input_integer("Необходимо ввести целое число. Повторите ввод: ")


def create_list():
    size = input_integer("Какой размер будет у списка? ")
    new_list = [(input_integer("Введите %d число: " % (i+1)))
                for i in range(size)]
    return new_list


def convert_list_to_set(new_list):
    new_set = set(new_list)
    return new_set


def output():
    new_list = create_list()
    new_set = convert_list_to_set(new_list)
    amount = len(new_set)
    print("В списке", new_list, "встречается %d различных чисел" % amount)


output()
