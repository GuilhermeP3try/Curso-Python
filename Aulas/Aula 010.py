'''nome = str(input('Qual e o seu nome ? '))
if nome == 'Guilherme':
    print('Que nome lindo vc tem !!!')  
else:
    print('Seu nome e tao nomral !')    
print('Bom dia, {}'.format(nome))'''

# estrutura simples e sem o else 

n1 = float(input('Digite a primeira nota :'))
n2 = float(input('Digite a segunda nota :'))
m = (n1+n2)/2
print ('A sua media foi {:.1f}'.format(m))
if m>= 6.0:
    print('Voce esta na media, PARABENS !')
else:
    print ('Voce esta fora da medeia, ESTUDE MAIS !')