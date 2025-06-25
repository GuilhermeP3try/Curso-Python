lista = ('APRENDER','PROGRAMAR','LINGUAGEM',
         'PYTHON','CURSO','GRATIS',
         'ESTUDAR')
for c in lista:
   print(f'\nNa palavra {c.upper()} temos',end=' ')
   for letra in c:
      if letra.lower() in 'a,e,i,o,u':
         print(letra , end=' ')

    