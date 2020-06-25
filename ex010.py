# Crie um programa que leia 4 nomes e sorteie um deles

from random import choice

n1 = str(input('Digite o 1º nome: '))
n2 = str(input('Digite o 2º nome: '))
n3 = str(input('Digite o 3º nome: '))
n4 = str(input('Digite o 4º nome: '))

sorteio = choice([n1 , n2 , n3 , n4])

print('O sorteado foi: {}'.format(sorteio))
