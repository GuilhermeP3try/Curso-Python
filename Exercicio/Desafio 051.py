t = int(input('Primeiro Termo: '))
r = int(input('Razao: '))
d = t + (10 - 1) * r
print('Primeiro termo: {}'.format(t))
print('Razao: {}'.format(r))
for pa in range (t,d+r,r):
   print('{}'.format(pa),end=' \u2192 ')
print('ACABOU')