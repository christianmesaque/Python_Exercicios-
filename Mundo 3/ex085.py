pares = list()
impares = list()
for c in range(1, 8):
    num = int(input(f'Digite o {c}° valor: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print('===' * 10)
pares.sort()
print(f'Os valores pares digitados foram: {pares}')
impares.sort()
print(f'Os valores ímpares digitados foram: {impares}')