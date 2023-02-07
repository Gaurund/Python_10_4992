s = 'a a a b c a a d c d d'
s = s.split()
print(s)
result_dic = {} #dictionary в который будем класть счетчики какой символ сколько раз встречается
new_s = [] # новый лист в который будем класть по условию в задаче
for i in s:
    if i not in result_dic: # если еще нет в словаре, первый раз
        new_s.append(i) # кладем наш символ
        # result_dic[i] = result_dic.get(i, 0)+ 1 # с помощью метода get возвращаем в словарь наш символ искусственно добавляя 1
    else: # если уже есть в словаре, значит пошли повторы
        new_s.append(f'{i}_{result_dic[i]}') # кладем значение с постфиксом и значение из словаря
    result_dic[i] = result_dic.get(i, 0) + 1
print(*new_s)