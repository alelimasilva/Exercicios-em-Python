from time import sleep

def leiaint(string, ini, fim):
    aux = str(input(string)).strip()
    while not aux.isnumeric() or int(aux) < ini or int(aux) > fim: # verifica se é numerico e se esta entre as opçoes.
        print('\033[1;31mERRO! Digite um numero valido\033[m')
        aux = str(input(string)).strip()
    return int(aux)


def cabecalho(frase):
    print('-'*50)
    print(f'{frase:^50}')
    print('-' *50)


def menu():
    lista = ['Cadastrar Pessoas', 'Ver Pessoas Cadastradas', 'Criar novo Arquivo', 'Sair do Sistema']

    c = 1 
    for item in lista:
        print(f'\033[1;33m{c} - \033[1;34m{item}\033[m')
        c += 1
    print('-' *50)
    opcao = leiaint('\033[1;33mSua Opção: \033[m', 0, len(lista))
    escolha(opcao)


def escolha(opcao):
    lista1 = ['Criar Arquivo', 'Voltar para o menu']
    if opcao == 1:
        cabecalho('Cadastrar Pessoas')
        while True:
            nome = str(input('Nome: ')).capitalize()
            idade = leiaint('Idade: ', 0, 250)
            arq = open("Cadastro.txt", "at")
            arq.write(f'{nome};{idade}\n')
            arq.close()
            escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
            while escolha not in 'SN':
                escolha = str(input('Resposta não válida! Quer continuar? [S/N] ')).strip().upper()[0]
            if escolha == 'N':
               cabecalho('MENU PRINCIPAL')
               menu() 

    if opcao == 2:
        cabecalho('Ver Pessoas Cadastradas')
        arq = open("Cadastro.txt", "r")
        for linha in arq:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos.')
        input('Pressione <enter> para continuar')
        cabecalho('MENU PRINCIPAL')
        menu()
        arq.close()
    if opcao == 3:
        cabecalho('Criar novo Arquivo')
        print('\033[1;31mCaso crie um novo arquivo,\nos dados ja existentes serão EXCLUIDOS.\n\033[m')
        c1 = 1 
        for item in lista1:
            print(f'\033[1;33m{c1} - \033[1;34m{item}\033[m')
            c1 += 1
        print('-' *50)
        opcao1 = leiaint('\033[1;33mSua Opção: \033[m', 0, len(lista1))
        if opcao1 == 1:
            arq = open("Cadastro.txt", "w")
            cabecalho('Arquivo Criado com Sucesso')
            sleep(1)
            cabecalho('MENU PRINCIPAL')
            menu()            
        if opcao1 == 2:
            cabecalho('MENU PRINCIPAL')
            menu()
    if opcao == 4:
        sleep(1)
        cabecalho('Sair do Sistema')
        sleep(1)
        exit()
