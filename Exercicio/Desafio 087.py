matriz =[[0,0,0], [0,0,0],[0,0,0]]
par =soma =maior = 0
for linha in range (3):
   for coluna in range(3):
      matriz[linha][coluna]= int(input(f'Digite um valor para {linha,coluna}: ')) 
print('=-'*20)
for linha in range (3):
   for coluna in range (3):
      if matriz[linha][coluna] %2==0:
         par += matriz[linha][coluna]
      print (f'[{matriz[linha][coluna]:^5}]',end='')
   print()
print('=-'*20)
for coluna in range(3):
   soma+= matriz[coluna][2]
for linha in range(3):
   if matriz[1][linha] >maior:
      maior=matriz[1][linha]
print(f'A soma dos Numeros pares sao {par}')
print(f'O maior numero da segunda {maior} ')
print(f'A soma da coluna 3 e de {soma} ')
