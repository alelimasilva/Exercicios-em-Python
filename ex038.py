''' Aprimore o desafio anterior, mostrando no final:
            A) A soma de todos os valores pares digitados
            B) A soma dos valores da terceira coluna
            C) O maior valor da segunda linha '''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_p = soma3 = maior = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite o valor {[l]}{[c]}: '))
        if matriz[l][c] % 2 == 0:
            soma_p += matriz[l][c]
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            if matriz[l][c] >= maior:
                maior = matriz[l][c]
        if c == 2:
            soma3 += matriz[l][c]
print('-=-'*30)
for l in range(3):
    for c in range(3):
        print(f'{matriz[l][c]:^5} ',end='')
    print()
print('-=-'*30)
print(f'A soma de todos os elementos pares vale: {soma_p}')
print(f'A soma de todos os elementos da 3ª coluna vale: {soma3}')
print(f'O maior elemento da 2ª linha é: {maior}')
