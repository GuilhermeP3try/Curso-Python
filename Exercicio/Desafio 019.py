from random import choice
print('Quem ira limpar o quadro ? ')
a1 = input ('Digite o Primeiro Aluno ')
a2 = input ('Digite o Segundo Aluno ')
a3 = input ('Digite o Terceiro Aluno ')
a4 = input ('Digite o Quarto Aluno ')
alunos = [a1,a2,a3,a4]
escolha = choice (alunos)
print ('Quem ira Limpar o Quadro e {}'.format(escolha))