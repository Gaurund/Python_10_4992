'''
Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
'''

grade_list = [1, 3, 3, 3, 4]


def low_grades(grade_list):
    for i in range(len(grade_list)):
        if grade_list[i] > 3:
            grade_list[i] = 1
    return grade_list


print(grade_list)
print(low_grades(grade_list))
