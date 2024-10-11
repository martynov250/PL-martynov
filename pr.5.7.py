s = input('введите строку ')
print(len(s))
k=''
for i in range(len(s) // 2):
     if s[i] == 'п':
         k=k+'*'
     else:
        k=k+s[i]
for i in range(i+1, len(s)):
    k=k+s[i]
print(k)