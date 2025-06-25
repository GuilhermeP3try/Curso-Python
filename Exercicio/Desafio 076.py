listagem = ('Lapis', 1.75,'Borracha', 2,'Caderno', 15.90,'Estojo', 25 )
print ('-'*40)
print('LISTAGEM DE PRECOS'.center(40))
print ('-'*40)
for c in range(0,len(listagem)):
    if c %2 == 0:
        print(f'{listagem[c]:.<30}',end=' ')
    else:
        print(f'R${listagem[c]:>7.2f}')
print ('-'*40)