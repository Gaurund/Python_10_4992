'''
Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
'''

string = "a a a b c a a d c d d"
str_list = string.split()
occurrences = dict()
for i in str_list:
    if i not in occurrences:
        occurrences[i] = 0
        print(i, end=' ')
    
    else:
        occurrences[i] += 1
        print(f'{i}_{occurrences[i]}', end=' ')
