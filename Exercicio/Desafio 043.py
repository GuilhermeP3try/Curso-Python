p = float(input('Digite o Seu Peso: '))
a = float(input('Digite a sua altura: '))
a2 = a/100
imc = p / (a2*a2)

if imc < 18.5:
    print('Voce esta abaixo do peso, o seu IMC e de {:.2f}'.format(imc))
elif   18.5 >= imc <= 25:
    print('Voce esta com o peso ideal, o seu IMC e de {:.2f}'.format(imc))
elif imc >= 25 and imc <= 30:
    print ('Voce esta com sobre peso, o seu IMC e de {:.2f}'.format(imc))
elif imc >=30 and imc <= 40:
    print('Voce esta com obesidade, o seu IMC e de {:.2f}'.format(imc))
elif imc > 40:
    print('Voce esta com obesidade morbida, o seu IMC e de {:.2f}'.format(imc))
else:
    print('Tente novamente')