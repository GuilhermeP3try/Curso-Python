temp = []
princ = []
maior = menor = 0

while True:
    temp.append(input('Nome: ').capitalize())
    temp.append(int(input('Peso: ')))
    if len(princ) == 0:
         maior = menor = temp[1]
    if temp[1] > maior:
        maior = temp [1]
    if temp[1] < menor :
        menor = temp [1]
    princ.append(temp[:])
    temp.clear()
    res = input('Quer continuar ? [S/N] ').upper()
    if 'N' in res:
        break
print('=-'*20)
print(f'Foram {len(princ)} cadastros')
print(f'O maior peso foi {maior}.Foi de ',end='')
for pessoa in princ:
    if pessoa [1] == maior:
        print(f'{pessoa[0]}')
print(f'O menor peso foi {menor}. Foi de ',end= '')
for pessoa in princ:
    if pessoa [1] == menor:
        print(f'{pessoa[0]}')
print()