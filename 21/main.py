'''
Задача №21. Решение в группах
Напишите программу для печати всех уникальных
значений в словаре.
Input: 
[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
Примечание: Список словарей задан изначально.
Пользователь его не вводит
'''

dic_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]

uniq_values = set()
for i in dic_list:
    for value in i.values():
        uniq_values.add(value.strip())

print(uniq_values)