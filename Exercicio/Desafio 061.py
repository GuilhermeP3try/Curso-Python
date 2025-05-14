t = int(input('Primeiro Termo: '))
r = int(input('Razao: '))
contador = 1
while contador <= 10:
    print(t,end=' \u2192 ')
    t += r
    contador += 1
    
print('acabou')
