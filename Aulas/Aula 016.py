# tuplas sao imutaveis
lanche = ('Hamburguer','sucos','pizza','pudim')
print (lanche)

for cont in range (0,len(lanche)): # se quiser saber a posicao um op 
    print(lanche[cont])

for comida in lanche:# ou usar for pos, comida in enumerate(lanche)
    print (comida)