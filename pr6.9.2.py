A = []
B = []
A1 = []
B1 = []
for i in range(10):
    A.append(int(input('Введите элементы массива A ')))
for i in range(10):
    B.append(int(input('Введите элементы массива B ')))
for i in range(10):
    A1.append(B[i])
    B1.append(A[i])


print('Преобразованный массив A ', A1)
print('Преобразованный массив B ', B1)