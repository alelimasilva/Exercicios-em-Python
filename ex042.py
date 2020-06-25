''' Crie um programa onde quatro jogadores joguem um dado e tenham resultados aleatórios.
    Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
    sabendo que o vencedor tirou o maior número no dado. '''

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador_1': randint(1, 6),
        'jogador_2': randint(1, 6),
        'jogador_3': randint(1, 6),
        'jogador_4': randint(1, 6)}
ranking = list()
print('-=-VALORES SORTEADOS-=-')
for k,v in jogo.items():
    print(f'O {k} tirou {v}.')
    sleep(1)
print('-=-'*10)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # itemgetter(1) ordena os valores '0' ordena as chaves.
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
