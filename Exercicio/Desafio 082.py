lista = []
impar = []
par = []
while True:
    num = int(input('Digite um numero: '))
    lista.append(num)
    res = input('Deseja continuar ? [S/N] ').strip().upper()
    while res not in 'SN':
        res = input('Deseja continuar ? [S/N] ').strip().upper()
    if 'N' in res:
        break
for c in lista:
    if c %2 == 0:
           par.append(c)
    elif c %2 != 0:
           impar.append(c)
print('-='*10)
print(f'Lista completa {lista}')
print(f'Lista de pares {par}')
print(f'Lista impar {impar}')