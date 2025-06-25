from time import sleep
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
um = 0
print('='*30)
print('BANCO GP'.center(30))
while True:
    print('='*30)
    saque = input('Que valor Voce quer sacar ? ')
    while not saque.isdigit():
        saque = input('Valor invalido. Digite um nuemero: ')
    print('CALCULANDO ...')
    sleep (1)
    saque = int(saque)
    cinquenta = saque //50
    resto = saque %50
    vinte = resto // 20
    resto = resto %20
    dez = resto // 10
    resto = resto%10
    cinco = resto // 5
    resto = resto %5
    um = resto // 1
    resto = resto %1
    break
print (f'Notas {cinquenta} de €50 ')
print (f'Notas {vinte} de €20 ')
print(f'Notas {dez} de €10 ')
print(f'Notas {cinco} de €5 ')
print(f'Notas {um} de €1')
sleep (1)
print('='*30)
print('OBRIGADO E ATE A PROXIMA'.center(30))
print('='*30)