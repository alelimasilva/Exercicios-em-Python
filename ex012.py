#Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome: ')).strip()
print('Nome com letras maiusculas: {}'.format(nome.upper()))
print('Nome com letras minusculas: {}'.format(nome.lower()))
total = len(nome) - nome.count(' ')
print('Total de letras: {}'.format(total))
primeiro = nome.split()
print('Numero de letras no primeiro nome: {}'.format(len(primeiro[0])))