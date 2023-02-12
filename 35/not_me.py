def simple_num(x):
    # for i in range(2,x): # Исходный вариант
    for i in range(2, int(x**0.5)+1): # Вариант с сокращением цикла для экономии ресурсов
        if x % i == 0:
            return 'NO'
    return 'YES'


n = int(input('Введите число: '))

print(simple_num(n))