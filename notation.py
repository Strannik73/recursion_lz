def func(number, scale):
        if scale > number:
            return str(number)
        return func(number // scale, scale) + str(number % scale)

scale = int(input('система счисления : '))
number = int(input('число : '))
 
print('перевод : ',number, "(10)=", func(number, scale), "(", scale, ")", sep="")
