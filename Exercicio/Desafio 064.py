n = 0
cont = 0
p = 999
soma = 0
while True:
   n = int(input('DIGITE UM NUMERO [999 PARA PARAR] ')) 
   if n !=p:
    cont += 1
    soma +=n

   elif n == p:
     break
   
print (f'Voce digitou {cont} e a soma entre eles foi {soma}')