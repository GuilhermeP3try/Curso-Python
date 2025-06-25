alunos = []
cont = 0
while True:
    nome = input('NOME: ').capitalize()
    nota1 = int(input('NOTA 1: '))
    nota2 = int(input('NOTA 2: '))
    per = input('QUER CONTINUAR ? [S/N] ').strip().upper()
    media = (nota1+nota2) /2  
    alunos.append([nome,[nota1,nota2],media])
    if 'N' in per:
        break
print('-'*30)
print(f"{'No.':<4}{'NOME':<10}{'MEDIA':>6}")
for c , aluno in enumerate(alunos):
     print(f'{c:<4}{aluno[0]:<10}{aluno[2]:>6.1f}')
print('-'*30)
while True:
    nota= input('Mostrar a Nota de Qual Aluno ? Digite [999]')
    if '999' in nota:
        break
    if nota == c:
        c = aluno[0]
        print(c)