n = int(input('введите n '))
s = 0
f = 1
for x in range(1, n+1):
    f = f * x
    print(f)
    s = s + f
print(s)
