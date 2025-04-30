v = float(input('Quilometragem da Viagem: '))
if v<200:
    print('A sua viagem ira custar €{}'.format(v*0.5))
else:
    print('A sua viagem ira custar €{}'.format(v*0.45))