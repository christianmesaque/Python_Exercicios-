from datetime import date
anoAtual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1,8):
    anoNascimento = int(input("Em que ano a {}° pessoa nasceu? ".format(c)))
    idade = anoAtual - anoNascimento
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print("Ao todo tivemos {} pessoas maiores de idade".format(totmaior))
print("E também tivemos {} pessoas menores de idade".format(totmenor))