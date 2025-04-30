v = float(input('Velocidade do Carro: '))
l = 80
if v>l:
    exedente = v-l
    print('Voce foi multado no valor de €{:.1f} '.format(exedente*7))
    print('Diminua a Velocidade !!!')
else:
    print('Parabens Voce esta no limite aceitavel da via !!!')