'''Crie um programa que 'pense' um numero de 0 a algum valor e peça
para o usuario tentar adivinhar se esta certo. '''

from random import randint
x = int(input('Digite um valor: '))
computador = randint(0, x)
tentativa = 0
acertou = False
print('Digite o numero que pensei de 0 a {}.\n'.format(x))
while not acertou:
    player = int(input('Qual o seu palpite? '))
    tentativa+=1
    if player == computador:
        acertou = True
    else:
        if computador > player:
            print('Mais... Tente novamente.')
        else:
            print('Menos... Tente novamente.')
print('Você Ganhou em {} tentativas.'.format(tentativa))
