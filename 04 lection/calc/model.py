x = 0
y = 0


def init(a, b):
    global x, y
    x = a
    y = b


def sum():
    return x + y


init(11, 12)

print(x, y)
