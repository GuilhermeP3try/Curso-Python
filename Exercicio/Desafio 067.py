cont = 0
ultimo = 10
n = int(input('Quer ver a tabuada de qual valor ? '))
while True:
    print('-'*30)
    if n < 0:
        break
    cont += 1
    valor = n*cont
    print(f'{cont} X {n} = {valor}')
    if cont == ultimo:
        cont = 0
        n = int(input('Quer ver a tabuada de qual valor ? '))
       
   
