'''
15. Иван Васильевич пришел на рынок и решил
купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз
потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9

'''


def input_integer(msg):
    num = input(msg)
    try:
        return (int(num))
    except ValueError:
        return input_integer("Необходимо ввести целое число. Повторите ввод: ")


def get_number():
    num = input_integer("Введите количество арбузов число: ")
    while num < 1:
        num = input_integer(
            "Пожалуйста, введите неотрицательное число. Повторите ввод: ")
    return num


def watermelon():
    amount = get_number()
    max_weight = input_integer("Введите массу 1 арбуза: ")
    min_weight = max_weight
    for i in range(1, amount):
        weight = input_integer("Введите массу %d арбуза: " % (i+1))
        if weight > max_weight:
            max_weight = weight
        if weight < min_weight:
            min_weight = weight
    print(min_weight, max_weight)


watermelon()
