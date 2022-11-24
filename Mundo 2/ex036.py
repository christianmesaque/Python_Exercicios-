valorCasa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
anos = int(input('Quanos anos de financiamento? '))
prestacao = valorCasa / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valorCasa, anos, prestacao))
if prestacao <= (30 / 100 * salario):
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
