velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO!, o limite máximo é 80KM/H ')
    multa = (velocidade-80) * 7
    print('Deve pagar a multa de R${}'.format(multa))
else:
    print('Tenha um bom dia, a sua velocidade está na média.')