from time import sleep
print ('Gostaria de um emprestimo ?\nNos passe o Valor da casa, seu salario e em quanto tempo quer pagar.')
casa = float(input('Valor da Casa: '))
salario = float(input('O teu Salario: '))
tempo = int(input('Em quanto tempo quer pagar: ')) 
meses = tempo * 12
vcasa = casa/meses
salario1 = salario *0.30
print('Calculando...')
sleep(1)

if vcasa <= salario1:
    print('Parabens foi Aceito o seu imprestimo de €{:.2f} por mes'.format(vcasa))
else:   
    print('Voce nao podera comprar a casa, pois as parcelas sao de €{:.2f} muito altas para o seu salario'.format(vcasa))