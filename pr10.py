a = []
b = []
file = open("D:\\pr10\\Martynov_Mikhail_Vladimirovich_UB-41_vvod.txt.txt", 'r+')
for line in file:
    print(line.strip())
    a.append([int(x) for x in line.strip().replace(' ', '')])

print(a)
a1 = []
a2 = []
k = -1
m = -1
file = open("D:\\pr10\\Martynov_Mikhail_Vladimirovich_UB-41_vvod.txt.txt", 'r+')
n = len(a[1])
print('n =', n)

for i in range(n):
    for j in range(n):
        if i != j:
            a2.append(a[i][j])
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
print(a[1])

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
file = open("D:\\pr10\\Martynov_Mikhail_Vladimirovich_UB-41_vivod.txt.txt", 'r+')

for i in range(n):
    for j in range(n):
        print(file.write(f'{a[i][j]} '))
    print(file.write('\n'))