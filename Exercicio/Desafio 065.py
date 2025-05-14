contador = soma = numero = 0
sn = ''
primeiravez = True

while True:
    numero = int(input('Digite um numero '))
    soma += numero
    contador +=1
    if primeiravez :
        maior = numero
        menor = numero
        primeiravez = False
    else:
        if numero> maior:
            maior= numero
        if numero<menor:
            menor = numero

    sn = input('Quer continuar ? [S/N]').strip().upper()
    if sn != 'S':
        break
    
print(f'Voce digitou {contador} numeros e a media foi {soma/contador:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')