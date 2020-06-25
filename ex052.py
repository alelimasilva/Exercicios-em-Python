''' Faça um programa que tenha uma função chamada ficha(), que receba
    dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
    O programa deverá ser capaz de mostrar a ficha do jogador, mesmo
    que algum dado não tenha sido informado corretamente. '''

def ficha(nome = '<desconhecido>', gol = 0):
    print(f'O jogador {nome} fez {gol} gol(s).')


nome = str(input('Nome do jogador: ')).strip().capitalize()
gol = str(input('Número de gols: ')) # lendo como str para nao dar erro
if gol.isnumeric(): # analisa se gol e inteiro
    gol = int(gol)
else:
    gol = 0
if nome == '': # analisa se o nome esta vazio se estiver, chama apenas com o segundo parametro
    ficha(gol=gol)
else:
    ficha(nome, gol)
