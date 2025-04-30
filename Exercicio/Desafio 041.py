from datetime import datetime
print('Para se inscrever basta colocar o seu nome e ano de nascimento.')
nome = input('Nome: ').title()
ano = int(input('Ano de Nascimento: '))
idade = datetime.now().year - ano
if idade<=9:
    print('Parabens {}, voce ira competir na MIRIM'.format(nome))
elif idade <=14:
    print('Parabens {}, voce ira competir na INFANTIL'.format(nome))   
elif idade <=19:
    print('Parabens {}, voce ira competir na JUNIOR'.format(nome))
elif idade<=20:
    print('Parabens {}, voce ira competir na SENIOR'.format(nome))
else:
    print('Parabens {}, voce ira competir na MASTER'.format(nome))

