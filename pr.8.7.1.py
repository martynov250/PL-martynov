n = int(input('введите число строк '))
a = []
a1 = []
a2 = []
k = -1
m = -1

for i in range(n):
    b = []
    for j in range(n):
        b.append(int(input('введите массив ')))
    a.append(b)

for i in range(n):
    for j in range(n):
        if i != j:
            a2.append(a[i][j])
print(a)

s = len(a2) // 2

for j in range(s):
    a1.append(int(input('введите одномерный массив ')))

for i in range(n):
    for j in range(1, n):
        if (i != j) and (i < j):
            k = k + 1
            a[i][j] = a1[k]

for i in range(n):
    for j in range(n):
        if (i != j) and (i > j):
            m = m + 1
            a[i][j] = a1[m]

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()