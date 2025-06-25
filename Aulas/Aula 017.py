# Listas
# .append('') adiciona item no final da lista
# .insert(0,'') insere em qualquer lugar 
# del string [] exclui o indice
# string.pop( ) exclui o indice mas precisa colocar qual,se n ele exclui so o utlimo
# string.remuve ('') vc remove o item e o indice 
# string.sort() coloca em ordem 
# string.sotr(reverse=True) em ordem de tras para frente  
# len (string) conta quantos elementos 

'''num = [2,5,8,1]
num [2] =3
num.append(7)
num.sort(reverse=True)
num.insert(2,0)
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''

valores = []
'''valores.append(5)
valores.append(9)
valores.append(4)'''
for cont in range(0,5):# usa para pegar os numeors do telcado 
    valores.append(int(input('Digite um valor: ')))

'''for v in valores: # mostra os numeors sem os []
    print(f'{v}',end= ' ')'''
for c,v in enumerate(valores): # mostra a posicao e o valor 
    print(f'Na posicao {c} encontrei o valor {v} !')

a = [2,3,4,7]
# b = a #sincroniza a lista 
b = a [:] # faz uma copia

