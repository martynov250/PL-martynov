n = int(input('Введите длинну массива '))
x = []
y = []
for i in range(n):
    x.append(int(input('Введите элементы массива ')))
    print(x)
for i in range(n):
    y.append(x[i])
a = max(x)
b = min(x)
for i in range(n):
    if x[i] == max(x):
        y[i] = min(x)
for i in range(n):
    if x[i] == min(x):
        y[i] = max(x)


print ('максимум = ', a,  '   минимум = ', b)
print (y)
