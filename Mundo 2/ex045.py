from time import sleep
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('==' * 15)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('==' * 15)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('\033[30;47mEMPATE\033[m')
    elif jogador == 1:
        print('\033[30;42m JOGADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[30;41mCOMPUTADOR VENCE\033[m')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('\033[30;41mCOMPUTADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[30;47mEMPATE\033[m')
    elif jogador == 2:
        print('\033[30;42m JOGADOR VENCE\033[m')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('\033[30;42m JOGADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[30;41mCOMPUTADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[30;47mEMPATE\033[m')
    else:
        print('JOGADA INVÁLIDA!')

