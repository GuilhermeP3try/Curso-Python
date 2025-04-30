t = int(input('Digite um numero para saber a sua tabuada: '))
for r in range (1,11):
    resultado = t * r
    print ('{} X {} = {}'.format(t,r,resultado))