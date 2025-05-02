from datetime import datetime
atual = datetime.now().year
lm = 0
ln = 0

for c in range (1,7+1):
    ano = int(input('Em que ano a pessoa nasceu ? '))
    idade = atual - ano
    if idade >= 21:
        lm += 1
        
    else:
        ln += 1
print('Ao todo tivemos {} de maiores\nE tambem {} de menores'.format(lm,ln))
   