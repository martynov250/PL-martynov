a = int(input('Введите число '))
y = ''
y1 = ''
k = int
b = []
def f(x):
    global y
    global y1
    while x % 8 > 0:
        print(x % 8)
        y = str(x % 8) + y
        x = (x // 8)
    y1 = '0' * (10 - len(y)) + y
    return y1
print(f(a))
