times = ('palmeiras', 'internacional', 'fluminense' ,'corinthians', 'flamengo',
         'atlético-PR', 'atlético-MG', 'fortaleza', 'são paulo', 'américa-MG',
         'botafogo', 'santos', 'goias', 'redbull bragantino', 'coritiba', 'cuiba',
         'ceara', 'atlético-GO', 'avai', 'juventude')
print(f'Lista de times do Brasileirão 2022: {times}')
print('======' * 10)
print(f'Os últimos 4 colocados são: {times[16:]}')
print('======' * 10)
print(f'Times em ordem alfabética: {sorted(times)}')
print('======' * 10)
print(f'A juventude está na {times.index("juventude")+1}° posição')