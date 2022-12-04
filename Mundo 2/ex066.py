count = 0
n = s = 0
while True:
    n = int(input('Digite um número: [999 para parar] '))
    if n == 999:
        break
    count += 1
    s += n
print('A soma dos {} valores é {}'.format(count, s))
