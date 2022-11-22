velocidade = int(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você exedeu o limite permitido que é 80Km/h')
    print('Você deve pagar uma muita de R${:.2f}'.format((velocidade - 80) * 7))
print('Tenha um bom dia! Dirija com segurança!')