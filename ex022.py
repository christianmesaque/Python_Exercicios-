nome = input('Nome Completo: ').strip()
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em mainúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

