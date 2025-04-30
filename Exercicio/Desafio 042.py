print ('''Quer saber se com a medicas que voce tem da para fazer um triangulo?
E qual deles da para ser feito? 
       ''')
r1 = int(input('Digite o Primeiro Numero: '))
r2 = int(input('Digite o Segundo Numero: '))
r3 = int(input('Digite o Terceiro Numero: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:

    if r1 == r2 and r2 == r3 :
        print('Voce tem um triangulo EQUILATERO')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('Voce tem um triangulo ESCALENO')
    else :
        print ('Voce tem um triangulo ISOSCELES')

else:
    print('Nao da para fazer um triangulo com esses numeros')
    

  