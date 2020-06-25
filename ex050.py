''' Faça um programa que tenham uma lista chamada numeros e duas funções
    chamadas sorteia() e somaPar().
    A primeira função vai sortear X números e vai coloca-los dentro da lista
    e a segunda função vai mostrar a soma entre todos valores pares sorteados
    pela função anterior.'''

from random import randint
from time import sleep
numeros = list()

def sorteia(lista, total):
    num = cont = 0
    while cont < total:
        num = randint(0, 100)
        lista.append(num)
        cont += 1

def somap(numeros):
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    return soma


total = int(input('Quantos valores deseja sortear? '))
sorteia(numeros, total)
sleep(0.8)
print('Valores sorteados: ',end='')
for valor in numeros:
    sleep(0.4)
    print(f'{valor} ',end='')
sleep(0.8)
print()
print(f'Soma dos valores pares: {somap(numeros)}')
