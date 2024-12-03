A = int(input('введите число А '))
B = int(input('введите число B '))

def f(A, B):
    if A < B:
        print (A)
        f(A + 1, B)
        if A == B - 1:
            print(B)
    elif A > B:
        print (A)
        f(A - 1, B)
        if A - 1 == B:
            print(B)

print(f(A, B))
