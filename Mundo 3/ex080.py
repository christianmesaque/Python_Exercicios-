valores = list()
for c in range(1, 6):
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print("Adicionando a lista...")
    else:
        print('Valor repetido, não irei adiconar na lista...')
valores.sort()
print(f'Os valores digitados em ordem foram {valores}')
