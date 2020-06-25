''' Faça um programa que determine se uma frase é palindromo ou não.'''

frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.split()
frase = ''.join(frase)
inverso = ''
for letra in range(len(frase)-1, -1, -1):
    inverso += frase[letra]
# ao inves dor for pode colocar o comando "inverso = frase[::-1]"
print('Frase digitada: {}'.format(frase))
print('Frase invertida: {}'.format(inverso))
if frase == inverso:
    print('É palindromo.')
else:
    print('Não é palindromo.')
