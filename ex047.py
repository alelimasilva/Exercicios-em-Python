''' Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
          como parâmetro e mostre uma mensagem com o tamanho adaptável.
          Ex: escreva('Olá, Mundo!')
          Saída:
                -------------
                 Olá, Mundo!
                ------------- '''

def escreva(str):
    print('-'*(len(str) +4))
    print(f'  {str} ')
    print('-' *(len(str) +4))

escreva('Alexandre')
escreva('Uma frase bem grande para ver se adapta.')
escreva('FRASE MEDIA')