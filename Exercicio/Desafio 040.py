from time import sleep
print ('Qual e o seu Nome ?')
nome = input ().title()
print ('')
print('{} Digite as suas notas, para saber se passou de ano, esta de recuperacao ou  reprovou.'.format(nome))
print('')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
print('CALCULANDO ...')
sleep(1)
media = (n1 + n2 + n3)/3
if media<5:
    print('{}, Voce esta reprovado, a sua media foi {:.2f}.'.format(nome,media))
elif media >=5 and media <=6.9:
    print('{} Voce esta em recuperacao, sua media foi {:.2F}.'.format(nome,media))
else:
    print('{}, Parabens, voce passou de ano, a sua media foi {:.2F}.'.format(nome,media))