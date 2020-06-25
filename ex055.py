''' Faça um mini-sistema que utilize o interative Help do Python. O usuário
    vai digitar o comando e o manual vai aparecer. Quando o usuário digitar
    a palavra 'FIM' o programa se encerrará.
    Obs: Use cores. '''

from time import sleep

def header(str):
    print('\033[7m')
    print('-'*(len(str) +4))
    print(f'  {str} ')
    print('-' *(len(str) +4))
    print('\033[m')


while True:
    sleep(0.5)
    header('SISTEMA DE AJUDA PYHELP')
    escolha = str(input('Biblioteca ou função > ')).strip().lower()
    if escolha == 'fim':
        sleep(0.5)
        print('\033[1;30;44m')
        print('FINALIZANDO...')
        print('\033[m')
        sleep(0.5)
        break
    else:
        sleep(0.5)
        print('\033[1;30;44m')
        print(f'{help(escolha)}')
        print('\033[m')
