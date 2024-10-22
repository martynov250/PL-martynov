str = input('введите строку ')
s1 = '*'
for i in range(0, 2):
    if str[i] == 'g':
        str[i] = str[i] - ' ' + '*'
    else:
        s2 = str[i]
print(str)