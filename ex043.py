''' Crie um programa que leia nome, ano de nascimento e carteira de trabalho de uma pessoa e
    cadastre-os (com idade) em um dicionário se por acaso a CTPS (Carteira de Trabalho e Previdência Social)
    for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
    Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. '''

from datetime import date
dados = {}

dados['Nome'] = str(input('Digite seu nome: ')).strip().capitalize()
dados['Idade'] = date.today().year - int(input('Ano de nascimento: ')) # diminui o ano atual pelo de nascimento
dados['CTPS'] = int(input('Carteira de trabalho (Digite 0 se não tiver): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Sálario'] = float(input('Sálario: R$'))
    dados['aposentadoria'] = dados['Contratação'] - (date.today().year - dados['Idade']) + 35
print('-=-'*30)
for k, v in dados.items():
    print(f'{k} = {v}')
