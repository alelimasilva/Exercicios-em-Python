'''Crie um programa que 'pense' um numero de 0 a 5 e peça
para o usuario tentar adivinhar se esta certo. '''

from random import randint
n = randint(0, 5)
num = int(input('Digite o numero que pensei de 0 a 5.\n'))
if num == n:
    print('Acertou miseravi')
else:
    print('Errou trouxa')
    print('A resposta era: {}'.format(n))
