total = mil = count = menor = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    count += 1
    total += preco
    if preco >= 1000:
        mil += 1
    if count == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('------- FIM DO PROGRAMA -------')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custou R${menor:.2f}')
