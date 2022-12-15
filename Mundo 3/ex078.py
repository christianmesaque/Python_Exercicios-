valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)
print(f'O maior valor digitado foi {max(valores)} e sua posição é {valores.index(max(valores)) + 1}')
print(f'O menor valor digitado foi {min(valores)} e sua posição é {valores.index(min(valores)) + 1}')
