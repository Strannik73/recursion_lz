
def rty(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return n
    


a = int(input('введите первое число:  '))
b = int(input('введите второе число:  '))

print(rty( a, b ))

