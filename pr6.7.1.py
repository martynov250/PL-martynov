n = int(input('Ввеите длинну массива '))
s = 0
p = 1
x = []
for i in range (n):
    x.append(int(input()))
print (x)
for i in range (n):
    if x[i] % 2 == 0:
        s = s + x[i]
    else:
        p = p * x[i]
print('сумма = ',s)
print('произведение = ',p)