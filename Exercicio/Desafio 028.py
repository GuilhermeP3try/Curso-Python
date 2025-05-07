from random import choice
n = int(input('Digite um Numero: '))
pc = choice([0,1,2,3,4,5])
if n==pc:
    print('Parabens Voce Ganhou !' )
else:
    print('Voce Perdeu !') 