# Faça um programa que leia um numero real e mostre sua parte inteira.

from math import trunc

x = float(input('Digite um valor: '))

print('A parte inteira de {} vale {}'.format(x , trunc(x)))


'''Ou pode ser feito apenas convertendo o numero para inteiro  int(x)'''