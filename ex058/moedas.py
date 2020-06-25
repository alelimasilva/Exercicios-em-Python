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