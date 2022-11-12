preco = float(input('Preço do produto: '))
desconto = preco - (preco * 5) / 100
print('O produto que custava R${}, com desconto de 5% vai custar R${}'.format(preco, desconto))
