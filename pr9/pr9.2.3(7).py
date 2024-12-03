def f():
    x = int(input('->'))
    if x == 0:
        return
    else:
        print(x)
        x = int(input('->'))
        if x == 0:
            return
    f()
print(f())