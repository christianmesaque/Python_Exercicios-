while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for tab in range(1, 11):
        print(f'{n} x {tab} = {n * tab}')
print('PROGAMA TABUADA ENCERRADO.')
