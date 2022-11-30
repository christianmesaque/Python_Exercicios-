print('=====' * 5)
print('Sequência de Fibonacci')
print('=====' * 5)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
count = 3
while count <= n:
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    t1 = t2
    t2 = t3
    count += 1
print('FIM')
print('~' * 30)