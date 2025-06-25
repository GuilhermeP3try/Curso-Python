lis =[]
men = mai = 0
for c in range (0,5):
    lis.append(int(input(f'Digite um valor para a Posicao {c}')))
    if c == 0:
        mai = men = list[c]
    else:
        if lis[c] > mai:
            mai= lis[c]
        if lis[c] < men:
            men = lis[c]   
    #ex para descobrir o maior e o menor