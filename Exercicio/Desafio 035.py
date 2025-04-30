print ('Quer saber se com as retas q tem da para fazer um trinagulo ?')#
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print('Voce pode fazer um triangulo com essas medidas')
else:
    print('Nao tem como fazer um triangulo com essas medidas')