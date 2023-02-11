'''
Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes 
'''

def is_simple(num):
    if num < 4:
        return "YES"
    for i in range(2,num):
        if num % i == 0:
            return "NO"
    return "YES"

print(is_simple(int(input("Input a number: "))))