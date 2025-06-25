from time import sleep
print('='*30)
print('BANCO PETRY'.center(30))
print('='*30)
valor = int (input('VALOR DO SAQUE: '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced +=1
    else:
        if totced > 0:
            print(f'TOTAL DE {totced} CEDULAS DE €{ced}')
        elif ced == 50:
            ced =20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*30)
print('VOLTE SEMPRE'.center(30))
print('='*30)
