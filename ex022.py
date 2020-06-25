''' Faça um programa que joque jokempô contra você! '''

from random import randint
from time import sleep
comp = randint(0, 2)
escolha = ('Pedra', 'Papel', 'Tesoura')
print('JOKENPÔ')
jog = int(input('''Escolha sua jogada!
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
Resposta: '''))
if jog > 2:
    print('\n')
    print('=*=' * 100)
    print('Escolha ínvalida!!!!!')
else:
    print('\nJO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO !!!\n')
    sleep(1)
    print('=*=' * 100)
    if comp == jog:
        print('Empate!\nEscolhi \033[7m{}\033[m\nVocê escolheu \033[7m{}\033[m'.format(escolha[comp], escolha[jog]))
    elif comp == 0 and jog == 2 or comp == 1 and jog == 0 or comp == 2 and jog == 1:
        print('Ganhei!\nEscolhi \033[7m{}\033[m\nVocê escolheu \033[7m{}\033[m'.format(escolha[comp], escolha[jog]))
    else:
        print('Você ganhou!\nEscolhi \033[7m{}\033[m\nVocê escolheu \033[7m{}\033[m'.format(escolha[comp], escolha[jog]))

print('=*=' * 100)
