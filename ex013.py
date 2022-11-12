var = float(input('Qual é o salário do funcionario? '))
newS = var + (var * 15) /100
print('O funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(var, newS))
