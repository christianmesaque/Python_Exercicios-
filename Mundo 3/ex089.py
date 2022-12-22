dados = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('==='*10)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":<0}')
print('==='*10)
for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[2]:<8.1f}')
while True:
    print('==='*10)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(dados) - 1:
        print(f'Notas de {dados[opc][0]} são {dados[opc][1]}')
print('<<< VOLTE SEMPRE >>>')