salario = float(input('Qual o salário do funcionário? '))
if salario <= 1250:
    novoSalario = (15 / 100 * salario) + salario
else:
    novoSalario = (10 / 100 * salario) + salario
print('Quem ganhava R${:.2f} passa a receber R${:.2f}'.format(salario, novoSalario))
