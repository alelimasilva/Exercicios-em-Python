'''Faça um programa que leia um angulo e mostre o seno, cosseno e a tangente desse angulo'''

from math import cos, tan, sin, radians

n = float(input('Digite o angulo desejado: '))

n = radians(n)
print('Valor do seno: {:.2f}'.format(sin(n)))
print('Valor do cosseno: {:.2f}'.format(cos(n)))
print('Valor da tangente: {:.2f}'.format(tan(n)))

'''e necessario converter o angulo recebido pois a funçao sin, cos e tan so funciona
em radianos e a funçao 'radians' transforma o angulo em radianos'''

