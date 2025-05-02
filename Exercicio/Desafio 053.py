nome = input('Digite uma frase: ').strip().upper()
separar = nome.split()
juntar = ''. join(separar)
inverso = ''
for p in range (len(juntar)-1,-1,-1):
    inverso += juntar [p]
    if juntar == inverso:
        print('e uma palindromo')
    else:
        print('nao e um palindromo')