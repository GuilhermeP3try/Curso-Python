termo = int(input('Quantos termos voce quer mostrar ? '))
contador = 2
f1 = 0
f2 = 1
print(f'{f1} \u2192 {f2}',end=' \u2192 ')
while contador < termo:
    fibo = f1 + f2 
    f1 = f2
    f2 = fibo
    print (f'{fibo}',end=' \u2192 ')
    contador += 1 
print('fim')