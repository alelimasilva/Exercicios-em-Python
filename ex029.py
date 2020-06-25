''' Escreva um programa que tenha uma tupla com varias palavras
 e deve mostrar quais sao as vogais de cada palavra (nao usar acentos)'''

palavras = ('aprender', 'casa', 'cruzeiro',
            'programar', 'python', 'alexandre')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
