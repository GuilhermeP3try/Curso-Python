# while not
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n %2 == 0:
            par += 0
        else:
            impar += 1
print('voce digitou {} numeors pares e {} numeros impare!'.format(par,impar))