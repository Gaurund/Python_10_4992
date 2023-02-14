'''
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
'''

from random import randint

my_list = [randint(1,10) for _ in range(20)]
print(my_list)
my_list.sort()
count = 0
for i in range(1,len(my_list)):
    if my_list[i-1] == my_list[i]:
        count += 1
        
print(count)