def prime(n):
    i = 2
    flag = True
    while i < n and flag:
        if n % i == 0:
            flag = False
        i += 1
    if flag:
        return 'YES'
    return 'NO'

n = int(input())
print(prime(n))