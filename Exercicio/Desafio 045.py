from random import randint
from time import sleep
print ('''SUAS OPCOES :
[0] PEDRA
[1] PAPEL 
[2] TESOURA''')
j = int(input('QUAL E A SUA JOGADA ? '))
lista = ('PEDRA','PAPEL','TESOURA')
r = randint(0,2)

print('JO')
sleep(1)

print ('KEN')
sleep(1)

print('PO !!!')
sleep(1)

print ('=-'*11)

print ('COMPUTADOR JOGOU {}'.format(lista[r]))
print ('JOGADOR JOGOU {}'.format(lista[j]))

if r == 0:
    if j == 0:
        print ('EMPATOU')
   
    elif j == 1:
        print('VOCE GANHOU')
   
    elif j == 2:
     print('VOCE PERDEU')
   
    else:
        print ('OPCAO INVALIDA')

    
elif r == 1:
    if j == 0:
        print('VOCE PERDEU')

    elif j == 1:

        print('EMPATE')
    
    elif j == 2:
        print('VOCE GANHOU')

    else:
        print('OPCAO INVALIDA')
    
elif r == 2:
    if j == 0:
        print('VOCE GANHOU')

    elif j == 1:
        print('VOCE PERDEU')
    
    elif j == 2:
        print('EMPATE')
    
    else:
        print('OPCAO INVALIDA')
print('-='*11)