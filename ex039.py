''' Faça um programa que ajude um jogador da mega sena a criar palpites.
    O programa vai perguntar quantos jogos serão gerados e vai sortear
    6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista
    composta. '''

from random import randint
from time import sleep

lista = []
jogos = []
print('-'*40)
print(f'{"GERADOR DE JOGOS":^40}')
print('-'*40)
quant = int(input('Quantos jogos você deseja sortear? '))
tot = 1
while tot <= quant: # aqui conta quantos jogos seram feitos começando no 1º ate o numero desejado
    cont = 0 # contador para o numero de valores em cada jogo
    while True:
        num = randint(1, 60)
        if num not in lista: # caso o valor nao esteja na lista ele e adicionado
            lista.append(num)
            cont+=1
        if cont == 6:
            break
    lista.sort() # ordena a lista
    jogos.append(lista[:]) # faz uma copia para a principal
    lista.clear() # limpa a parcial
    tot += 1 # adiciona 1 jogo feito no total
print('-'*40)
print(f'{"SORTEANDO OS JOGOS":^40}')
print('-'*40)
for i,l in enumerate(jogos): # serve para printar os jogos pegando o indices e as listas dentro da lista principal
    sleep(1)
    print(f'Jogo {i+1}: {l}')
