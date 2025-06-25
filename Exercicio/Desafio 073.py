times = 'Palmeiras', 'Flamengo', 'Cruzeiro', 'Red Bull Bragantino', 'Ceará','Bahia', 'Fluminense', 'Corinthians', 'Atlético Mineiro', 'Botafogo', 'São Paulo','Mirassol', 'Vasco da Gama', 'Fortaleza', 'Internacional', 'Vitória', 'Grêmio', 'Juventude', 'Santos', 'Sport Recife'

print(f'Lista de time do Brasileirao :{times}')
print('-='*30)
print(f'Os 5 pimeiros sao {times[:5]}')
print('-='*30)
print(f'Os 4 ultimos sao {times[-4:]}')
print('-='*30)
print(f'Times em ordem alfabetica {sorted(times)}')
print('-='*30)
print(f'O inter esta na {times.index("Internacional")+1}')