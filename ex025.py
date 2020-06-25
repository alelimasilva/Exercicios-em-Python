''' Escreva um programa que mostra os N primeiros valores da sequencia fibonacci'''

n = int(input('Digite Quantos termos de fibonacci você deseja mostrar? '))
total = 0
a = 0
b = 1
if n <= 0:
    print('Invalido')
elif n == 1:
    print('{} ->'.format(a), end='')
elif n == 2:
    print('{} -> {} -> '.format(a, b), end='')
else:
    print('{} -> {} -> '.format(a, b), end='')
    for i in range(3, n+1):
        total = a + b
        print('{} -> '.format(total), end='')
        a = b
        b = total
print('Fim')
