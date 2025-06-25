from random import randint
from time import sleep
jogos = []
print('-'*40)
print('JOGA NA MEGA'.center(40))
print('-'*40)
quantidade = int(input('Quantos jogos voce quer que eu sorteie? '))
for c in range(quantidade):
    jogo = []
    for l in range(6):
        while True:
            sorteio = randint(1,60)
            if sorteio not in jogo:
                jogo.append(sorteio)
                break
    jogos.append(sorted(jogo))
print('\nSeus jogos Sorteados: ')
print('=-'*7,f'SORTEANDO {quantidade}','=-'*7)
for i,jogo in enumerate(jogos,start=1):
    print(f'JOGOS {i}: {jogo}')
    sleep(1)
print('-='*8,'BOA SORTE','-='*8)
   

     
            