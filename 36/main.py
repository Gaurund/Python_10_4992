'''
Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
ровно два аргумента, как, например, у операции умножения.
Ввод: 
print_operation_table(lambda x, y: x * y)

Вывод:
1 2 3 4 5 6
2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36 
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


def choose_wisely():
    operation_choice = input_integer(
        "Выберите операцию, которую хотите применить.\n1 - для сложения.\n2 - для вычитания.\n3 - для умножения.\n\n")
    while not 1 <= operation_choice <= 3:
        operation_choice = input_integer(
            "Выбор должен быть из этих трёх чисел! Повторите ввод: ")
    if operation_choice == 1:
        return (lambda x, y: x+y)
    elif operation_choice == 2:
        return (lambda x, y: x-y)
    return (lambda x, y: x*y)


def print_table(operation, rows, columns):
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            print(f"{operation(i, j):3}", end=" ")
        print(end="\n")


def output():
    columns = get_number("Введите количество столбцов в таблице: ",
                         "Ошибочное значение. Повторите ввод: ")
    rows = get_number("Введите количество строк в таблице: ",
                      "Ошибочное значение. Повторите ввод: ")
    operation = choose_wisely()
    print_table(operation, rows, columns)


output()
