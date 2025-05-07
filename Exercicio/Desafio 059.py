from time import sleep
p1 = int(input('Primeiro valor: '))
p2 = int(input('Segundo Valor: '))
op = 0
while op != 5:
    print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR  
>>>>> Qual e a sua opcao ? ''')
    op = int(input())
    sleep (1)
    if op == 1:
            somar = p1 + p2
            print('A soma entre {} + {} = {}'.format(p1,p2,somar))
            print('-'*30)
           
    elif op == 2:
            multiplicar = p1 * p2
            print('A multiplicacao de {} x {} = {}'.format(p1,p2,multiplicar))
            print('-'*30)
    elif op == 3:
           if p1 == p2:
                  print('{} e {} sao iguais'.format(p1,p2))
           elif p1 > p2 :
                  print('{} e maior que {}'.format(p1,p2))
           else:
                  print('{} e maior que {}'.format(p2,p1))
                  print('-'*30)
    elif op == 4:
           print('Informe os numeros novamente: ')
           p1 = int(input('Primeiro umero: '))
           p2 = int(input('Segundo Numero: '))  
           print('-'*30)         
    sleep(1)