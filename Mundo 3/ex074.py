from random import randint

numbers = (randint(1, 10), randint(1, 10), randint(1, 10),
    randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for c in numbers:
    print(f'{c} ', end='')
print(f'\nO maior valor sorteado foi {max(numbers)}')
print(f'O menor valor sorteado foi {min(numbers)}')