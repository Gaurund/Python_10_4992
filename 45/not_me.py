def sum_divided(n):
    div_sum = 1
    for i in range(2, (n//2)+1):
        if n % i == 0:
            div_sum += i
    return div_sum


def friendly_pairs(x):
    div_list = []
    for i in range(1, x + 1):
        y = sum_divided(i)
        if y > i and sum_divided(y) == i:
            div_list.append((i, y))

    return div_list


print(friendly_pairs(300))
