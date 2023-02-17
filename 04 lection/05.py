# list_1 = [x for x in range(1, 20)]
# print(list_1)
# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

data = '15 156 96 3 5 8 52 5'
data = list(map(int, data.split()))
print(data)