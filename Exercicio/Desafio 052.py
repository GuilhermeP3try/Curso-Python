'''num = int(input('Digite um numero: '))
for c in range(0,num + 1):
    if num %c == 0:
        print ('Esse numero {} nao e primo'.format(num))
print('{} e um numero primo'.format(num))'''

num = int(input('Digite um nuemro: '))
tot = 0
for c in range (1,num + 1):
    if num %c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO numeor {} foi divisivel {} vezes'.format(num,tot))
if tot == 2:
    print('E Primo')
else:
    print('Nao e Primo')