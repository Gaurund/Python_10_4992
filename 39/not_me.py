list1 = [int(input(f'Введите {i + 1}-е число: ')) for i in range(
    int(input('Введите количество элементов первого массива: ')))]
list2 = [int(input(f'Введите {j + 1}-е число: ')) for j in range(
    int(input('Введите количество элементов второго массива: ')))]
new_list = [el for el in list1 if el not in list2]
print(new_list)
