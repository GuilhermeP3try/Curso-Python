matriz =[[0,0,0], [0,0,0],[0,0,0]]
for linha in range (3):
   for coluna in range(3):
      matriz[linha][coluna]= int(input(f'Digite um valor para {linha,coluna}: ')) 
print('=-'*20)
for linha in range (3):
   for coluna in range (3):
    print (f'[{matriz[linha][coluna]}]',end='')  
   print()