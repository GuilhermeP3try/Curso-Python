from datetime import datetime
print ('Quer saber se esta na hora de alistar no exercito ?\nDigite: Sim ou Nao')
sn= input()

if sn.lower() =='nao':
    print('Ate a proxima')

nome = input('Digite o seu Nome: ').capitalize()
nascimento = int(input('Digite o ano de Nascimento: '))
idade = datetime.now().year - nascimento

if idade==18:
    print('{} esta na hora de se alistar'.format(nome))

elif idade<18:
    i1 = 18 - idade
    print('{} ainda nao e hora, faltam {} anos, procure mais informacoes em nosso site'.format(nome,i1))

else:
    i2 = idade -18
    print('{} ja passou {} anos, procure mais informacoes'.format(nome,i2))