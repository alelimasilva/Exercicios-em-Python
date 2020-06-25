''' crie uma função adicional chamada moeda()
    que consiga mostrar os valores como um valor monetário formatado. '''


from ex057 import moedas

valor = float(input('Digite o preço: R$'))
porcento = float(input('Digite a porcentagem: '))
print(f'A metade de {moedas.moeda(valor)} é {moedas.moeda(moedas.metade(valor))}')
print(f'O dobro de {moedas.moeda(valor)} é {moedas.moeda(moedas.dobro(valor))}')
print(f'O valor aumentado em {porcento}% é: {moedas.moeda(moedas.aumentar(valor, porcento))}')
print(f'O valor diminuido em {porcento}% é: {moedas.moeda(moedas.diminuir(valor, porcento))}')
