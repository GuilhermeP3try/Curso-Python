from random import randint
from time import sleep
pc = randint (0,10)
tentativas = 0
print('''Sou o seu computador ...
Acabei de pensar um nuemro entre 0 e 10.
Sera que voce consegue advinhar qual foi ?''')
print('-'*45)
sleep (1)

while True:
    palpite = int(input('Qual e o seu palpite ? '))
    tentativas += 1
    if palpite > pc:
        print('Menos... tente mais uma vez.')
    elif palpite < pc:
         print('Mais... tente mais uma vez')
    else:
        print ('Acertou com {} tentativas. Parabens !'.format(tentativas))
        break
