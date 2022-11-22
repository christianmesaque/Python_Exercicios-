days = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
total = days * 60 + 0.15 * km
print('O total a pagar é de R${}'.format(total))
