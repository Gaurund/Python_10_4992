'''
Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке

Ввод: 
пара-ра-рам рам-пам-папам па-ра-па-дам 

Вывод:
Парам пам-пам

'''


def count_syllables(phrase):
    counter = 0
    for letter in phrase:
        if letter in 'уеыаоэяиюУЕЫАОЭЯИЮ':
            counter += 1
    return counter

def output():
    hum = input("Введите бурчалку Винни-Пуха: ")
    phrases = hum.split()
    syllables = list(map(count_syllables, phrases))

    if min(syllables) == max(syllables):
        print("Парам пам-пам")
    else:
        print("Пам парам")


output()
