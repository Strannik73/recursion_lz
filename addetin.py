def gen_bin(M, prefix=''):   # M - количество разрядов, prefix - сюда наращиваются 
    if M == 0:
        print(prefix)
        return
 
    gen_bin(M - 1, prefix + '0')
    gen_bin(M - 1, prefix + '1')
 
gen_bin()