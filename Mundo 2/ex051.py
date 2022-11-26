print('==' * 20)
print('10 TERMOS DE UMA PA')
print('==' * 20)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = termo + (10 - 1) * razão
for c in range(termo, décimo + razão, razão):
    print('{} '.format(c), end='-> ')
print('ACABOU')