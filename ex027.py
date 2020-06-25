''' Crie um programa que mostre a tabuada do valor escolhido pelo usuario e pare quando o valor escolhido for negativo.'''

num = 0
while True:
    print('-=-'*20)
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-=-' * 20)
    if num < 0:
        break
    for i in range(1, 11):
        print(f'{num} X {i} = {num*i}')
print('Programa encerrado!!!')
