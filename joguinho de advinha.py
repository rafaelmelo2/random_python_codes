import random
print('Esse é o jogo do advinha! Seja Bem vindo.')
n1 = random.randint(0, 5)
n2 = int(input('Digite um número entre 0 e 5: '))

if n2 == n1:
    print('Parabéns, você ganhou da máquina')
else:
    print('Infelizmente a máquina ganhou de você')
print('A máquina tinha pensado {}'.format(n1))