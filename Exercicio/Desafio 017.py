from math import sqrt
o = float(input('Digite o cateto oposto: '))
a = float(input('Digite o cateto adjacente: '))
soma1 = pow(o,2)
soma2 = pow(a,2)
r = sqrt(soma1+soma2)
print ('A Hipotenuza e de {} '.format(r))