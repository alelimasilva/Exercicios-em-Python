''' Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados
    de cada pessoa em um dicionário e todos os dicionários em uma lista.
    No final, mostre:
            A) Quantas pessoas foram cadastradas;
            B) A média de idade do grupo;
            C) Uma lista com todas as mulheres;
            D) Uma lista com todas as pessoas com idade acima da média. '''

lista = list()
dados = dict()
pes_tot = idade_tot = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
    while dados['sexo'] not in 'MF':
        dados['sexo'] = str(input('Resposta não válida! Sexo[M/F]: ')).strip().upper()[0]
    dados['idade'] = int(input('Idade: '))
    lista.append(dados.copy()) # adicionando na lista uma copia dos dados da pessoa
    pes_tot += 1
    idade_tot += dados["idade"]
    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input('Resposta não válida! Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print('-=-'*30)
print(f'O total de pessoas cadastradas foi de {pes_tot}.')
print(f'A média de idade do grupo foi de {idade_tot/pes_tot:.2f} anos.')
print('As mulheres foram: ', end='')
for dados in lista:
    if dados['sexo'] == 'F':
        print(f'{dados["nome"]}',end=' ')
print()
print('Pessoas com idade acima da média: ',end='')
for dados in lista:
    if dados['idade'] >= (idade_tot/pes_tot):
        print(f'{dados["nome"]}', end=' ')
