'''
Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
ценность. В случае с английским алфавитом очки распределяются так:
● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только
английские, либо только русские буквы.
Ввод:
ноутбук
Вывод:
12
'''


def define_language(word):
    alphabet = set('QWERTYUIOPASDFGHJKLZXCVBNM')
    return not alphabet.isdisjoint(word.upper())


def count_score(word, points_per_char):
    count = 0
    for char in word.upper():
        for points in points_per_char.keys():
            if char in points_per_char[points]:
                count += points
    return count


def output():
    word = input('Input a word: ')
    if define_language(word):
        points_per_char = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP',
                           4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
    else:
        points_per_char = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ',
                           4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
    score = count_score(word, points_per_char)
    print(f"Слово \"{word}\" стоит {score} очков.")


output()
