idade = 0
contm = 0
conth = 0
cont = 0 
sexo = ''
print('-'*30)
print('CADASTRE UMA PESSOA'.center(30))
while True:
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F] : ').upper().strip()
    if idade >= 18:
        cont += 1
    if sexo == 'M': 
        conth += 1
    if sexo == 'F' and idade <=20 :  
        contm += 1
    pergunta = input('Quer continuar ? [S/N]').strip().upper()
    if pergunta == 'N':
        break
print('-'*30)
print(f'''Total de pessoas com mais de 18 anos {cont}
Ao todo temos {conth} homem cadastrado
E temos {contm} mulheres com menos de 20 anos''')
