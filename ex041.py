''' Faça um programa que leia o nome e média de um aluno, guardando também a situação
          em um dicionário. No final, mostre o conteúdo da estrutura na tela. '''

dados = {}

dados['Nome'] =  str(input('Digite seu nome: ')).strip().capitalize()
dados['Media'] = float(input('Digite sua media: '))
while dados['Media'] > 10 or dados['Media'] < 0:
    dados['Media'] = float(input('Digite sua media: '))
if dados['Media'] >= 6:
    dados['Situação'] = 'Aprovado'
if dados['Media'] < 6:
    dados['Situação'] = 'Reprovado'

for k, v in dados.items():
    print(f'{k} = {v}')
