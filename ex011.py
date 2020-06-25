'''Faça um programa que leia 4 nomes e faça e os coloque em uma ordem aleatoria'''

from random import shuffle

n1 = str(input('Digite o 1º nome: '))
n2 = str(input('Digite o 2º nome: '))
n3 = str(input('Digite o 3º nome: '))
n4 = str(input('Digite o 4º nome: '))

lista = [n1 , n2 , n3 , n4]
shuffle(lista)
print('A ordem é: ')
print(lista)
