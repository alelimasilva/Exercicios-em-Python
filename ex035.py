''' Faça um programa que leia o nome e peso de várias pessoas.
          guardando tudo em uma lista.
          No final, mostre:
            A) Quantas pessoas foram cadastradas;
            B) Uma listagem com as pessoas mais pesadas;
            C) Uma listagem com as pessoas mais leves; '''

dados = list()
pessoas = list()
pesados = list()
leves = list()
maior = menor = 0

while True:

    dados.append(str(input('Nome: ')).strip().capitalize())
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input('Resposta não válida! Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
for i in range(0, len(pessoas)):
    if i == 0: # coloca o primeiro como maior e menor
        maior = pessoas[i][1]
        menor = pessoas[i][1]
    if pessoas[i][1] == maior: # analisa se e igual ao maior e se for poe na lista de maiores
        pesados.append(pessoas[i][0])
    if pessoas[i][1] > maior: # analisa se e maior que o maior se for ele troca limpa a lista anterior e começa a montar denovo
        maior = pessoas[i][1]
        pesados.clear()
        pesados.append(pessoas[i][0])
    if pessoas[i][1] == menor: # analisa se e igual ao menor e se for poe na lista de menores
        leves.append(pessoas[i][0])
    if pessoas[i][1] < menor: # analisa se e menor que o menor se for ele troca limpa a lista anterior e começa a montar denovo
        menor = pessoas[i][1]
        leves.clear()
        leves.append(pessoas[i][0])

print('-=-'*30)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi : {maior}Kg. ',end='')
print(f'De: {pesados}.')
print(f'O menor peso foi : {menor}Kg. ',end='')
print(f'De: {leves}.')
