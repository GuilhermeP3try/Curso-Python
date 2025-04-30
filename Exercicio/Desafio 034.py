salario = float(input('Digite o seu Salario: '))
if salario>=1250:
    salario += salario*10/100
    print('O seu Salario tera 10% de almento sera de {:.2f} reais'.format(salario))
else:
   salario += salario*15/100
   print('O seu Salario tera 15% de almento sera de {:.2f} reais'.format(salario))