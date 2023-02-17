# my_list = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
# print(lambda my_list: [res.append((i, i*i)) for i in my_list if not i % 2] )

def select(f, col):
    return [f(x) for x in col if f(x)]

def where(f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x*x), res))
print(res)