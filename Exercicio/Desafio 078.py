valor = []
maior =  menor = c =c1 =0
for cont in range (0,5):
    num = (int(input(f'Digite um valor para a Posicao {cont}: ')))
    valor.append(num)
maior = valor [0]
menor = valor [0]
for num in valor:
    if num > maior:
        maior = num
       
    if num < menor:
        menor = num
        
print('=-'*19)
print(f'Voce digitou os valores {valor}')
print(f'O maior numero digitado foi {maior} nas posicoes ', end='')
for i, v in enumerate(valor):
    if v== maior:
        print(f'{i}... ',end= '')
print()
print(f'O menor numero digirado foi {menor} nas posicoes ', end='')
for i,v in enumerate(valor):
    if v==menor:
        print(f'{i}... ', end='')
print()