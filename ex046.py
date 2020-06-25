''' Faça um programa que tenha uma função chamada area(), que receba as dimeções
    de um terreno retangular(largura e comprimento) e mostre a área do terreno. '''


def area(a,b):
    area = a * b
    return area


a = float(input('Largura (M): '))
b = float(input('Comprimento (M): '))
print(f'A area do terreno {a:.2f} x {b:.2f} é de {area(a,b):.2f}m²')
