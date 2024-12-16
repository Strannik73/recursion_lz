g = int(input('введите конечный уровень:  '))

def pascal(n, joo=None):
    if joo is None:
        joo = [[1]]
    if n == 1:
        return joo
    else:
        prev_row = joo[-1]
        new_row = [1] + [sum(i) for i in zip(prev_row, prev_row[1:])] + [1]
        return pascal(n - 1, joo + [new_row])
    
print(pascal(g))