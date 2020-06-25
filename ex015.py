# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite seu nome: ')).strip()
nome = nome.lower()
print('Seu nome contem Silva? {}'.format('silva ' in nome))