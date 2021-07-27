n1 = float(input('Quantos KM você andou no carro? '))
n2 = int(input('Quantos dias você ficou com o carro? '))

total = (n2 * 60) + (n1 * 0.15)

print('O total a pagar é de R${:.2f}'.format(total))