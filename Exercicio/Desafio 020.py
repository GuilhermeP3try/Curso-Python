from random import shuffle
a1 = input('Digite o Primeiro Aluno ')
a2 = input('Digite o Segundo Aluno ')
a3 = input('Digite o terceiro aluno ')
a4 = input('Digite o Quarto Aluno ')

alunos = [a1,a2,a3,a4]

shuffle (alunos)

print ('a ordem {}'.format(alunos) )