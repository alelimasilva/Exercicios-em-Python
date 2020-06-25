'''  Crie um programa que leia varios numeros e so pare quando o usuario digitar '999'
e mostre na tela a soma entre eles e a quantidade de numeros digitados.'''

num = soma = cont = 0
while True:
    num = int(input('Digite um numero(999 para sair): '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Foram digitados {cont} numeros.\nE a soma vale {soma}.')
