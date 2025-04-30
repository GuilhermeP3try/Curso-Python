print('{:=^40}'.format(' LOJAS PETRY '))
preco = float(input('Preco das compras: '))
print ('''FORMAS DE PAGAMENTOS
[1] A VISTA DINHEIRO/CHEQUE
[2] A VISTA NO CARTAO
[3] EM ATE 2 X NO CARTAO
[4] 3 X OU MAIS NO CARTAO''')
opc = int(input('QUAL E A OPCAO ? '))

if opc == 1:
    p = preco - ( preco *10/100)
    print ('O VALOR FICA R${:.2f} COM 10% DE DESCONTO'.format(p))
elif opc == 2:
    p = preco *5/100
    print ('O VALOR FICA R${:.2f} COM 5% DE DESCONTO'.format(preco-p))
elif opc == 3:
     parcela = preco/2
     print ('O VALOR DA PARCELA R${:.2f}, TOTAL R${:.2f}'.format(parcela,preco))
elif opc == 4:
    p = preco+(preco*20/100)
    total = int(input('QUANTAS PARCELAS :'))
    parcela = p / total
    print ('O VALOR DA PARCELA FICA R${:.2f} COM ACRECIMO DE 20%, NO FINAL IRA PAGAR {:.2f}'.format(parcela,p))
else:
    print('ERRO, TENTE NOVAMENTE')
    