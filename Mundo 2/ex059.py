from time import sleep

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opção = 0
while (opção != 5):
    print('''
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa
        ''')
    opção = int(input('>>> Qual é a sua opção? '))
    if opção == 1:
        resultado = num1 + num2
        print('A soma entre {} e {} é {}'.format(num1, num2, resultado))
    elif opção == 2:
        resultado = num1 * num2
        print('O resultado de {} x {} é {}'.format(num1, num2, resultado))
    elif opção == 3:
        if num1 > num2:
            resultado = num1
        else:
            resultado = num2
        print('Entre {} e {} o maior é {}'.format(num1, num2, resultado))
    elif opção == 4:
        print('Informe os números novamente:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida. Tente novamente!')
    print('=====' * 6)
print('Fim do programa! Volte sempre.')