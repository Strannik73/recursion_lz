chislo = int(input('Введите число: '))
sistem = int(input('Введите систему счисления: '))


def ert(N: int, T: int) -> str:
    if N == 0:
        return '0'

    number = ''
    while N > 0:
        N, r = divmod(N, T)
        if r > 9:
            r = chr(ord('A') + r - 10)
        number = str(r) + number
    return number



print('конечное число: ',ert(chislo, sistem),)
