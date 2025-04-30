n1 = float(input('Digite o Primeiro Numero: '))
n2 = float(input('Digite o Segundo Numero: '))
n3 = float(input('Digite o Terceiro NUmero: '))

#Numero maior

if n1>n2:
    com1=n1
else:
    com1=n2
    
if com1>n3:
    com2=com1
else:
    com2=n3

#Numero menor

if n1<n2:
    com3=n1
else:
    com3=n2

if com3<n3:
    com4=com3
else:
    com4=n3
print('O maior Numero e {} e o menor e {}'.format(com2,com4))



