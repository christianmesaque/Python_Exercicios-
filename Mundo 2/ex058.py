from random import randint

count = 1
computador = randint(0, 10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
palpite = int(input('Qual é o seu palpite? '))
while (palpite != computador):
    if palpite < computador:
        print('Mais... Tente mais uma vez.')
        palpite = int(input('Qual é o seu palpite? '))
        count += 1
    else:
        print('Menos... Tente mais uma vez.')
        palpite = int(input('Qual é o seu palpite? '))
        count += 1
print('Acertou com {} tentativas. Parabéns!'.format(count))