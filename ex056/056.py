''' Crie um módulo chamado dados.py que tenha as funções incorporadas
    aumentar(), diminuir(), dobro() e metade().
    Faça também um programa que importe esse módulo e use algumas dessas
    funçóes. '''


from ex056 import moedas

valor = float(input('Digite o preço: R$'))
porcento = float(input('Digite a porcentagem: '))
print(f'A metade de {valor} é {moedas.metade(valor)}')
print(f'O dobro de {valor} é {moedas.dobro(valor)}')
print(f'O valor aumentado em {porcento}% é: {moedas.aumentar(valor, porcento)}')
print(f'O valor diminuido em {porcento}% é: {moedas.diminuir(valor, porcento)}')
