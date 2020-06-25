''' Crie um programa que jogue par ou impar com vc ate perder e no final mostre quantas vezes vc venceu.'''

from random import randint
from time import sleep
cont = 0
print('-=-'*20)
print('VAMOS JOGAR PAR OU IMPAR.')
print('-=-'*20)
while True:
    comp = randint(0, 10)
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar?  [P/I] ')).strip().upper()[0]
    num = int(input('Diga um valor: '))
    print('---'*20)
    print(f'Você jogou \033[1;32m{num}\033[m e o computador \033[1;32m{comp}\033[m.')
    sleep(1)
    resultado = num + comp
    if resultado % 2 == 0:
        print(f'Total: \033[1;32m{resultado}\033[m = \033[1;32mPar\033[m')
        resul = 'P'
    if resultado % 2 == 1:
        print(f'Total: \033[1;32m{resultado}\033[m = \033[1;32mImpar\033[m')
        resul = 'I'
    print('---' * 20)
    sleep(1)
    if escolha == resul:
        print('Você venceu!!!\nVamos jogar novamente...')
        sleep(1)
        print('-=-' * 20)
        cont+=1
    else:
        break
print(f'Game Over! Você venceu {cont} vezes.')
