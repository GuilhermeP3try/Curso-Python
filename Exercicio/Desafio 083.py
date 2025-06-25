exp = input('Digite a expressao: ')
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb ==')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print('A sua expressao esta valida')
else:
    print('A sua expressao e invalida')