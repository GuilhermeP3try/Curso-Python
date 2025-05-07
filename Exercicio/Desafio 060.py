n = int(input('''Digite um numero para 
caulcar seu Fatorial: '''))
f = 1
while n > 0:
    f *= n
    n -= 1
print(f'O fatorial e :{f}')
