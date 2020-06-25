''' Reencreva a função leiaInt(), incluindo agora
    a possibilidade da digitação de um número de tipo inválido.
    Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade. '''


def leiaint(numero):
    while True:
        try:
            aux = int(input(numero))
        except(ValueError, TypeError):
            print('\33[31mERRO! Informe um valor INTEIRO corretamente...\33[m')
            continue
        else:
            return aux


def leiafloat(numero):
    while True:
        try:
            aux = float(input(numero))
        except(ValueError, TypeError):
            print('\33[31mERRO! Informe um valor INTEIRO corretamente...\33[m')
            continue
        else:
            return aux


inteiro = leiaint('Digite um numero inteiro: ')
real = leiafloat('Digite um numero real: ')
print(f'O usuario digitou o valor inteiro -> {inteiro} e o real -> {real}')
