''' Crie um programa que leia uma lista e mostre no final a lista completa, so com os pares e so com os impares'''

lista = []
par = []
impar = []

while True:

    num = int(input('Digite um valor: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    if num % 2 == 1:
        impar.append(num)

    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input('Resposta não válida! Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'Lista completa: {lista}')
print(f'Lista de numeros pares: {par}')
print(f'Lista de numero impares: {impar}')
