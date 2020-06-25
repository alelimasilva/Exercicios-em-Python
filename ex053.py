''' Crie um programa que tenha a função leiaint(), que vai funcionar de forma
    semelhante a função input() do python, só que fazendo a validação para aceitar
    apenas um valor númerico.
    Ex:
    n = leiaint('Digite um n: ') '''

def leiaint(string):
    aux = str(input(string)).strip()
    while not aux.isnumeric(): # verifica se é numerico, se nao ele le novamente
        print('\033[1;31mERRO! Digite um numero valido\033[m')
        aux = str(input(string)).strip()
    return aux

n = leiaint('Digite um numero inteiro: ')
print(f'Você digitou o numero {n}')
