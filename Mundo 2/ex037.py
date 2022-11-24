valor = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
escolha = int(input('Sua escolha: '))
if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(valor, bin(valor)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}'.format(valor, oct(valor)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(valor, hex(valor)[2:]))
else:
    print('Opção inválida! Tente novamente.')
