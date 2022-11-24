print('====== LOJAS GUANABARA ======')
valorCompras = float(input('Preço das comprar: R$'))
print('''FORMAS DE PAGAMENTOS
[1] à vista dinheiro/pix
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')
formaPagamento = int(input('Qual é a forma de pagamento? '))
if formaPagamento == 1:
    avista = valorCompras - valorCompras * 10 / 100
    print('Sua compra de R${:.2f} à vista vai custar R${:.2f}'.format(valorCompras, avista))
elif formaPagamento == 2:
    cartãoAvista = valorCompras - valorCompras * 5 / 100
    print('Sua compra de R${} à vista no cartão vai custar R${}'.format(valorCompras, cartãoAvista))
elif formaPagamento == 3:
    print('Sua compra será parcelada em 2x de R${}'.format(valorCompras, valorCompras / 2))
elif formaPagamento == 4:
    qtdParcelas = int(input('Quantas parcelas? '))
    juros = valorCompras * 20 / 100
    print('Sua compra será parcelada em {}x de R${} COM JUROS'.format(qtdParcelas, (valorCompras + juros) / qtdParcelas))
    print('Sua compra de R${} vai custar {} no final'.format(valorCompras, valorCompras + juros))
else:
    print('Opção de pagamento INVÁLIDA. Tente novamente!')