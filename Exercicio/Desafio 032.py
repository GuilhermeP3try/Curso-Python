ano = int(input('Para saber se o ano e Bisexto ou nao.\nDigite o ano: '))
if ano%4!=0:
    print('Nao e Bisexto')

elif ano%100!=0:
    print('Nao e Bisexto')
elif ano%400==0:
    print('O ano e Bisexto')
else:
    print('Nao e Bisexto')    

