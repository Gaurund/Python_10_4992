'''
Задача №19. Решение в группах
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
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


def shift_list_right(new_list, shift):
    shift = shift % len(new_list)
    shifted_list = new_list[-shift:] + new_list[:-shift]
    return shifted_list


def output():
    new_list = create_list()
    print(new_list)
    shift = input_integer("На сколько значений сдвигаем? ")
    shifted_list = shift_list_right(new_list, shift)
    print(shifted_list)


output()
