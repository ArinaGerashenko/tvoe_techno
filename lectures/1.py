import math
print('Введите последовательно коэффициенты (a,b,c) уравнения: a*x^2+b*x+c=0\n')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a!=0:
    D = b*b-4*a*c
    if D>0:
        x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
        x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
        print('x1 = ',x1,'; x2 = ',x2)
    elif D==0:
        x = (-b)/(2*a)
        print('x1 = x2 = ',x)
    elif D<0:
        print('Вещественных корней нет!')
elif (a == 0) and (b == 0) and (c!=0):
    print('Ошибка! Заданно неверное уравнение!')
elif (a == 0) and (b == 0) and (c==0):
    print('Ошибка! Все коэффициенты являются нулевыми!')
elif (a == 0):
    x = (-c)/b
    print('x = ',x)
else:
    print('Ошибка!')
