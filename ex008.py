'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
e calcule o valor da hipotenusa'''

from math import hypot

n1 = float(input('Digite o valor do cateto oposto: '))
n2 = float(input('Digite o valor do cateto adjacente: '))

print('O valor da hipotenusa é: {:.3f}'.format(hypot(n1 , n2)))
print('{:.3f}'.format((((n1**2) + (n2**2)) ** (1/2))))



'''Desta forma tambem funciona:   (((n1**2) + (n2**2)) ** (1/2))   '''
