t = int(input('Primeiro Termo: '))
r = int(input('Razao: '))
contador = 0
total = 10
while contador <= total :
    print(t,end=' \u2192 ')
    t += r
    contador += 1
    if contador == total:
        mais = int(input('Quantos numeros voce quer mostrar a mais ? Se deseja sair pressione [0] '))
        if mais == 0:
                break
         
        total += mais
        

       

            
print(f'Progressao finalizada com {contador} termos')




