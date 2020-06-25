'''' Crie um programa que vai ler varios numeros e colocar em uma lista e depois mostre:
  quantos numeros foram digitados
  a lista em ordem decrescente
  se o valor 5 esta presente na lista '''

lista = []

while True:

    num = int(input('Digite um valor: '))
    lista.append(num)

    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input('Resposta não válida! Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print('-=-'*30)
print(f'O total de numeros foi: {len(lista)}')
print(f'A lista em ordem decrescente é: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('Contem o valor 5 na lista.')
else:
    print('O valor 5 nao esta contido na lista.')
