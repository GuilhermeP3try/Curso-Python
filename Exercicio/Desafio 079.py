lista = []
while True:
    l=(int(input('Digite um valor: ')))
    if l in lista:
        print('Valor duplicado ! Nao vou adicionar ...')
    else:
        lista.append(l)
        print('Valor adicionado com sucesso ...')
    sn = input('Voce quer continuar ? [S/N] ').upper().strip()
    if sn == 'N':
        break
print (sorted(lista))
