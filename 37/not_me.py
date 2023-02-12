from random import randint

n = 6


def recurs(x):
    if x == 0:
        return

    number = int(input()) # randint(0, 10)
    recurs(x-1)
    print(number, end=" ")
    

recurs(n)