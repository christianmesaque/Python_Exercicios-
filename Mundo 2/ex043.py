peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal!')
elif imc >= 18.5 and imc < 25:
    print('PARABÉNS, Peso ideal.')
elif imc > 25 and imc <= 30:
    print('Você esta com SOBREPESO!')
elif imc > 30 and imc <= 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')