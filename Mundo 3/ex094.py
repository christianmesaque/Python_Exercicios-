lista = list()
dados = dict()
soma = media = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: [M/F] '))
    if dados['sexo'] not in "MmFf":
        print('ERRO! Por favor, digite apenas M ou F.')
        dados['sexo'] = str(input('Sexo: [M/F] '))
    dados['idade'] = int(input('idade: '))
    soma += dados['idade']
    lista.append(dados.copy())
    resp = str(input('Quer continuar? [S/N] '))
    if resp not in "SsNn":
        print('ERRO! Por favor, digite apenas S ou N.')
        resp = str(input('Quer continuar? [S/N] '))
    elif resp in "Nn":
        break
print("===" * 10)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
media = soma / len(lista)
print(f'B) A média de idade é de {media:.1f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] in "Ff":
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')