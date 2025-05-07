sexo = ['M','F']
s = ''
while s not in sexo:
    s = input('Informe o sexo: [M/F] ').upper().strip()[0]
    if s in sexo:
        print ('Sexo {} registrado com sucesso'.format(s))
    else:
        print('Dados invalidos. Por favor, Informe o seu sexo:')
        