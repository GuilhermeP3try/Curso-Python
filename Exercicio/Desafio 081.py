count = 0
lista = []
while True:
    num = int(input('Digite um Numero: '))
    count +=1
    lista.append(num)
    pergunta = input('Voce deseja continuar ? [S/N]').strip().lower()
    if 'n' in pergunta:
        break
print('=-'*15)
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente {lista}')    
print(f'Voce digitou {count} elementos')
if 5 in lista:
    print('O 5 faz parte da lista')
else:
    print('O 5 nao faz parte da lista')

