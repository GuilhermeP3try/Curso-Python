nome = ba =''
preco = total = barato = caro= 0


print ('-'*30)
print ('LOJA PETRY'.center(30))
while True:
    print ('-'*30)
    nome = input('Nome do Produto: ')
    preco = float(input('Preco: '))
    total += preco
    res = input('Quer Continuar ? [S/N]').upper()
    while res not in 'SN':
        res = input('Quer Continuar ? [S/N]').upper()
    if preco >= 1000:
        caro += 1
    if barato == 0 or preco < barato:
        barato = preco
        ba = nome
    if res == 'N':
        break
print ('-'*7,'FIM DO PROGRAMA','-'*7)
print (f'O total da compra foi de R${total:.2f}')
print(f'Temos {caro} produtos custando mais de R$1000.00')
print(f'O produto mais barato {ba} que custa {barato:.2f}')



