from random import randint
from time import sleep
computador = randint(0, 5) #Computador "PENSA" em um número
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta advinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Você ganhou! Eu pensei no número {}'.format(computador))
else:
    print('Eu venci! Eu pensei no número {}'.format(computador))
