''' Crie um programa onde o usuário possa digitar sete valores númericos
          e cadastre-os em uma única lista que mantenha separados os valores
          pares e ímpares. No final, mostre os valores pares e ímpares em ordem
          crescente. '''

lista = [[], []]
num = int(input('Quantos valores deseja digitar? '))
print('-=-'*30)
for i in range(num):
    valor = int(input(f'Digite o {i+1}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    if valor % 2 == 1:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Valores pares em ordem crescente: {lista[0]}')
print(f'Valores impares em ordem crescente: {lista[1]}')
