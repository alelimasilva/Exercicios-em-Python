''' Modifique as funções que foram criadas para que elas
    aceitem um paràmetro a mais, informando se o valor retornado por elas
    vai ou não ser formatado pela função moeda(), desenvolvida no ex anterior. '''

from ex058 import moedas

valor = float(input('Digite o preço: R$'))
porcento = float(input('Digite a porcentagem: '))
print(f'A metade de {moedas.moeda(valor)} é {moedas.metade(valor, True)}')
print(f'O dobro de {moedas.moeda(valor)} é {moedas.dobro(valor, True)}')
print(f'O valor aumentado em {porcento}% é: {moedas.aumentar(valor, porcento, True)}')
print(f'O valor diminuido em {porcento}% é: {moedas.diminuir(valor, porcento, True)}')
