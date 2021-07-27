salario = float(input('Qual seu salário atual? R$'))
aumento = float(input('E quantos porcentos recebeu de aumento?' ))

novo = salario + (salario * aumento / 100)


print('O seu salário de R${}, aumentou para R${}'.format(salario, novo))