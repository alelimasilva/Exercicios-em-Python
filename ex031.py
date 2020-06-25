''' Crie um programa em que o usuario digite valores ate quando desejar
 mas nao possa deigitar valores repetidos e no final mostre a lista em ordem crescente.'''

lista = []

while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Adicionado com sucesso!')
    else:
        print('Valor já se encontra na lista.')
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if r in 'N':
        break
print('-=-'*30)
lista.sort()
print(f'A lista em ordem crescente é: {lista}')
