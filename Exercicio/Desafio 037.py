n = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversao:
      [1] Converter para BINARIO
      [2] Converter para OCTAL
      [3] Converter para HEXADECIMAL''')
op = int(input('Sua opcao: '))
if op == 1:
    print('{} Convertido para BINARIO e igual a {}'.format(n,bin(n)[2:]))
elif op==2 :
    print('{} Convertido para OCTAL e igual a {}'.format(n,oct(n)[2:]))
elif op==3:
    print('{} Convertido para HEXADECIMAL e igual a {}'.format(n,hex(n)[2:]))
else:
    print('RESPOSTA INVALIDA !!!')