lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = lar * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(lar, alt, area))
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(area / 2))