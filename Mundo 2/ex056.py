maioridadehomem = 0
nomevelho = ''
mulheres = 0
somaidades = 0
for p in range(1, 5):
    print("----- {}° PESSOA -----".format(p))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidades = somaidades + idade
    media = somaidades / 4
    if p == 1 and sexo in "M":
        maioridadehomem = idade
        nomevelho = nome
    if sexo == "M" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == "F" and idade < 20:
        mulheres += 1



print("A média de idade do grupo é de {} anos.".format(media))
print("O homem mais velho tem {} anos e se chama {}.".format(maioridadehomem, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos.".format(mulheres))