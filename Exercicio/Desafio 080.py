ordem = []
while True:
    if len(ordem) < 6:
        n = int(input('Digite um numero: '))
    else:
        break
    if n in ordem:
        print('Nao vou adicionar, numero repetido ...')
    else:
        print('Adicionado com sucesso ! ')
    for i, valor in enumerate(ordem):    
        if n  < ordem:
            ordem.insert(n)
        else:
            ordem.append(n)
