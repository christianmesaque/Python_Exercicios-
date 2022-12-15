valores = list()
while True:
    n = (int(input('Digite um valor: ')))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    next = str(input('Quer continuar? [S/N] '))
    if next in 'Nn':
        break
valores.sort()
print(f'Você digitou os valores {valores}')