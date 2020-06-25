''' Escreva um programa que leia um inteiro e peça
pro usuario escolher qual base sera convertido.
1- binario
2- octal
3- hexadecimal '''

num = int(input('''Digite um numero para ser convertido.
Sua opção: '''))

esc = int(input('''Digite 1 para binario.
Digite 2 para octal.
Digite 3 para hexadecimal.
Sua opção: '''))

if esc == 1:
    print('O numero {} em binario é: {}'.format(num, bin(num)[2:]))
elif esc == 2:
    print('O numero {} em octal é: {}'.format(num, oct(num)[2:]))
elif esc == 3:
    print('O numero {} em hexadecimal é: {}'.format(num, hex(num)[2:]))
else:
    print('\033[1;31;40mAlternativa Invalida.\033[m')
