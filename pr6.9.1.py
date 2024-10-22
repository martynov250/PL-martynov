N = int(input('Введите число элементов массива '))
x = []
y = []
for i in range(N):
    x.append(int(input('Введите элементы массива ')))
    print(x)
for i in range(N):
    y.append(abs(x[i]))
print('Минимальный по модулю элемент ', min(y))
print('эелементы массива в обратном порядке ', x[::-1])