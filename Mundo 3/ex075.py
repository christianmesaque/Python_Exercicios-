
numbers = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print(f'Você digitou os valores {numbers}')
print(f'O valor 9 apareceu {numbers.count(9)} vezes')
if 3 in numbers:
    print(f'O valor 3 apareceu  na {numbers.index(3)+1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in numbers:
    if n % 2 == 0:
        print(n, end=' ')