''' Faça um programa que leia 5 numeros e guarde em uma lista no final mostre o maior e o menor elemento
 das lista e suas respectivas posições.'''

lista = []
x = 5 # numero de elementos
maior = menor = 0
for v in range(0, x):
    lista.append(int(input('Digite o valor: ')))
    if v == 0:
        maior = menor = lista[v]
    else:
        if lista[v] > maior:
            maior = lista[v]
        if lista[v] < menor:
            menor = lista[v]
print(f'O maior elemento é \033[1;34m{maior}\033[m na ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'\033[1;34m{i}ª\033[m ', end='')
print('posição.')
print(f'O menor elemento é \033[1;34m{menor}\033[m na ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'\033[1;34m{i}ª\033[m ', end='')
print('posição.')
