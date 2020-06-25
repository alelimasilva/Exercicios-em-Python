# Faça um programa que leia algo pelo teclado e mostre na tela
# o tipo primitivo e todas informações possiveis sobre ele.


n = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(n)))
#sempre ira retornar str pois nao foi especificado no input
print('Só tem espaços? {}'.format(n.isspace()))
print('É um numero? {}'.format(n.isnumeric()))
print('É alfabético? {}'.format(n.isalpha()))
print('É alfanumérico? {}'.format(n.isalnum()))
print('Está em maiúsulas? {}'.format(n.isupper()))
print('Está em minúsculas? {}'.format(n.islower()))
print('Esta capitalizada? {}'.format(n.istitle()))
