def leiaint(string):
    aux = str(input(string)).strip()
    while not aux.isnumeric(): # verifica se é numerico, se nao ele le novamente
        print('\033[1;31mERRO! Digite um numero valido\033[m')
        aux = str(input(string)).strip()
    return int(aux)


def header(frase):
    print('-'*50)
    print(f'{frase:^50}')
    print('-' *50)
    print('\033[1;33m1 - \033[1;34mVer pessoas cadstradas\033[m')
    print('\033[1;33m2 - \033[1;34mCadastrar nova pessoa\033[m')
    print('\033[1;33m3 - \033[1;34mSair do sistema\033[m')
    print('-' *50)
    opcao = leiaint('\033[1;33mSua Opção: \033[m')

