from datetime import date

anoAtual = date.today().year
anoNasc = int(input('Ano de nascimento: '))
idade = anoAtual - anoNasc
print('Quem nasceu em {} tem {} anos em {}.'.format(anoNasc, idade, anoAtual))
if idade < 18:
    print('Ainda faltam {} anos para o alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(anoAtual + (18 - idade)))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE.')
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(anoAtual - (idade - 18)))
