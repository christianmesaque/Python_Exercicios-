print('====' * 10)
print('CADASTRE UMA PESSOA')
print('====' * 10)
maior = 0
homens = 0
mulheres = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres} mulheres com menos de 20 anos.')
