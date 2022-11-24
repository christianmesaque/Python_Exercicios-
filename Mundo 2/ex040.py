nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {} e {} a média do aluno é {}.'.format(nota1, nota2, media))
if media < 5:
    print('O aluno está REPROVADO.')
elif media >= 5 and media < 7.0:
    print('O aluno está de RECUPERAÇÃO.')
elif media >= 7.0:
    print('O aluno está APROVADO.')