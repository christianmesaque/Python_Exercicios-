valores = list()
lista_par = list()
lista_impar = list()
while True:
    n = int(input('Digite um número: '))
    if n not in valores:
        valores.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
    resp = str(input('Quer continuar? [S/N] '))
    if resp in "Nn":
        break

print(f'A lista completa é {valores}')
print(f'A lista de pares é {lista_par}')
print(f'A lista de ímpares é {lista_impar}')