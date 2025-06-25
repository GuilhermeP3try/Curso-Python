num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite o ultimo numero: ')))
print (f'Voce Digitou os Valores {num}')
print (f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 aparaceu na {num.index(3)+1} posicao')
else:
    print ('O numero 3 nao foi digitado')
print(f'OS valores pares digitados fomram',end=' ')
for n in num:
    if n %2 == 0:
        print (n)
  