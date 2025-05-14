from random import randint
cont = 0
print ('=-'*15)
print ('VAMOS JOGAR PAR OU IMPAR')
print ('=-'*15)
while True:
    jogador = int(input('Diga um valor: '))
    pi = input('Par ou Impar [P/I]').strip().upper()[0]
    print ('='*30)
    pc = randint (0,10)
    resultado = jogador + pc
    cont += 1
    if pi == 'P' and resultado %2 == 0:
        print (f'Voce ganhou o numero {resultado} e PAR')
        print('Vamos jogar Novamente ...')
        print ('='*30)
    elif pi == 'I' and resultado %2 !=0:
        print(f'Voce ganhou o numero {resultado} e IMPAR')
        print('Vamos jogar Novamente ...')
        print ('='*30)
    else:
        print('Voce perdeu !')
        print('=-'*15)
        print(f'GAME OVER ! Voce venceu {cont} vezes, o resultado foi {resultado}')
        break
