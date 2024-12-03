n = int(input('введите число строк '))
a = []
a1 = []
a2 = []
A = []
c = []
aa = []

for i in range(n):
    b = []
    for j in range(n):
        b.append(int(input('введите двумерный массив ')))
    a.append(b)

for i in range(n):
    for j in range(n):
        if i == j:
            a1.append(int(a[i][j]))
for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            a2.append(int(a[i][j]))

A = a1 + a2

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()

print()

print(a1)
print(a2)

print()

print(A)
A1 = sum(A)
print(A1)

for i in range(n):
    for j in range(n):
        if i % 2 != 0:
            a[i][j] = a[i][j] / A1

print()

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()