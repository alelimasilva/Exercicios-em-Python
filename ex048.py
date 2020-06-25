'''Faça um programa que tenha uma função chamada contador(),
          que receba três parâmetros: inicio, fim e passo e realize a contagem.
          Seu programa tem que realizar três contagens atráves da função criada:
            A) De 1 até 10, de 1 em 1
            B) De 10 até 0, de 2 em 2
            C) Uma contagem personalizada '''

from time import sleep
def contador(inicio, fim, passo):
    print('---'*10)
    print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}.')
    if passo < 0:
        passo *= -1 # mudando o sinal do passo para positivo
    if inicio <= fim:
        while(inicio <= fim):
            sleep(0.5)
            print(f'{inicio}',end=' ')
            inicio += passo
        sleep(0.5)
        print('FIM!')
        sleep(0.5)
    elif inicio >= fim:
        while(inicio >= fim):
            sleep(0.5)
            print(f'{inicio}',end=' ')
            inicio -= passo
        sleep(0.5)
        print('FIM!')
        sleep(0.5)


#contador(1, 10, 1)
#contador(10, 0, 2)
print('---'*10)
print('Personalize a contagem.')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
while passo == 0:
    passo = int(input('Passo: '))
contador(inicio, fim, passo)
