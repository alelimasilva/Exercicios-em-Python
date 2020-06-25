def dobro(valor, format=False):
    if format == True:
        return moeda(valor*2)
    else:
        return valor*2


def metade(valor, format=False):
    if format == True:
        return moeda(valor / 2)
    else:
        return valor/2


def aumentar(valor, porcento, format=False):
    x = (valor * porcento) / 100
    if format == True:
        return moeda(valor + x)
    else:
        return valor + x


def diminuir(valor, porcento, format=False):
    x = (valor * porcento) / 100
    if format == True:
        return moeda(valor - x)
    else:
        return valor - x


def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')


def resumo(valor, porcento):
    print('-'*45)
    print('RESUMO DO VALOR'.center(45))
    print('-' * 45)
    print(f'A metade de \033[1;34m{moeda(valor)}\033[m é: \033[1;34m{metade(valor, True)}\033[m')
    print(f'O dobro de \033[1;34m{moeda(valor)}\033[m é: \033[1;34m{dobro(valor, True)}\033[m')
    print(f'O valor aumentado em \033[1;34m{porcento}%\033[m é: \033[1;34m{aumentar(valor, porcento, True)}\033[m')
    print(f'O valor diminuido em \033[1;34m{porcento}%\033[m é: \033[1;34m{diminuir(valor, porcento, True)}\033[m')
    print('-' * 45)


def leianum(numero):
    valido = False
    while not valido:
        entrada = str(input(numero)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print('\033[1;31mErro! Digite um número válido.\033[m')
        else:
            valido = True
            return float(entrada)

