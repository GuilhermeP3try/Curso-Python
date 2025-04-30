nome = str(input('digite o seu nome: '.title())).strip().upper()
print ('O seu nome tem {} A '.format(nome.count('A')))
print ('O primero A se encontra na posicao {}'.format(nome.find('A')+1))
print ('O ultimo A se encontra na posicao {}'.format(nome.rfind('A')+1))
