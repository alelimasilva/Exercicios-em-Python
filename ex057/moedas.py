def dobro(valor):
    return valor*2


def metade(valor):
    return valor/2


def aumentar(valor, porcento):
    x = (valor * porcento) / 100
    return valor + x


def diminuir(valor, porcento):
    x = (valor * porcento) / 100
    return valor - x


def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')