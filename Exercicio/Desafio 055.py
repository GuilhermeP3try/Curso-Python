for c in range(1,6):
    peso = float(input('Peso da {} pessoa :'.format(c)))
    if c == 1 : 
        maior = peso
        menor =  peso
      
    else:
        if peso > maior :
            maior = peso
        if peso < menor:
            menor = peso
print ('Maior peso {}kg, menor peso {}kg'.format(maior,menor))