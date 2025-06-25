numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito',
           'nove','dez','doze','treze','catorze','treze','quinze',
           'dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    n = int(input('Digite um numero de 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Voce digitou o numero {numeros[n]}')
        res = input('Voce desaja continuar ? [S/N]').upper()
        if res == 'N':
            break
    else:
        print('Tente novamente. ',end='')

