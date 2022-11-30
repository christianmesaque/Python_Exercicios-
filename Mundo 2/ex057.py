sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while (sexo not in 'MF'):
    sexo = str(input('Dados inválidos. Por favor, tente novamente: ')).strip().upper()
print('Sexo {} registrado com sucesso!'.format(sexo))
