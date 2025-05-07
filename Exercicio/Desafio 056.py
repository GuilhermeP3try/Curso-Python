somaidade = 0
mediaidade = 0
maioridadeh = 0
nomevelho = ''
m20 = 0 

for p in range (1,5):
    print('---------- {}ª ----------'.format(p))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ' )
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomevelho = nome
    if idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        m20 += 1
print ('-'*30)
mediaidade = somaidade /4        
print ('A media de idade do grupo {}\nMulheres que tem menos de 20 anos {}\nO homem mais velho {}'.format(mediaidade,m20,nomevelho))        

            

    