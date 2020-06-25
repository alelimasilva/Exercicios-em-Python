''' Faça um programa que tenha a função maior(), que recebe vários parâmetros
    com valores inteiros.
    Seu programa tem que analisar todos os valores e dizer qual deles é o maior. '''

from time import sleep

def maior(*num):
    if len(num) == 0:
        maior = 'Nenhum valor foi encontrado'
    else:
        maior = num[0]
        cont = 1
        while cont < len(num):
            if num[cont] > maior:
                maior = num[cont]
            cont+=1
    print('---'*18)
    print('Os valores são: ', end='')
    for valor in num:
        sleep(0.3)
        print(f'{valor}',end=' ')
    print()
    sleep(1)
    print(f'Foram analisados um total de {len(num)} numero(s).')
    sleep(1)
    print(f'O maior valor foi: {maior}')
    sleep(1)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
