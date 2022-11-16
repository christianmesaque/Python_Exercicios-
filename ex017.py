from math import hypot
catOposto = float(input('Comprimento do cateto oposto: '))
catAdjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(catOposto, catAdjacente)
print("A hipotenusa vai medir {:.2f}".format(hipotenusa))
