''' Crie um programa que gerencie o aproveitamento de um jogador de futebol.
    O programa vai ler o nome do jogador e quantas partidas ele jogou.
    Depois vai ler a quantidade de gols feitos em cada partida.
    No final, tudo isso será guardado em um dicionário, incluindo o total de gols
    feitos durante o campeonato. '''

jogador = {}

jogador['nome'] = str(input('Qual o nome do jogador? ')).strip().capitalize()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

jogador['gols'] = []  # Adicionando lista de gols na ficha do jogador
totalgols = 0

for i in range(partidas):
    jogador['gols'].append(int(input(f'\tGols da {i+1}º partida: ')))
    totalgols += jogador['gols'][i]

jogador['total'] = totalgols
print('-=-'*30)
print(jogador)

print('-=-'*30)
for k,v in jogador.items():
    print(f'{k} = {v}')

print('-=-'*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')

for k,v in enumerate(jogador["gols"]):
    print(f'=> Na partida {k},fez {v} gols.')

print(f'Um total de {totalgols} gols.')
