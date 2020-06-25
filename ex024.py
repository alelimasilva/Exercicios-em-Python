''' Crie um programa que leia o nome, idade e o sexo de X pessoas
e diga:
- a media das idades
- a idade e o nome da pessoa mais velha
- quantos homens e mulheres foram cadastrados.'''

media = 0
velho = 0
nomevelho = ''
numf = 0
numm = 0
x = int(input('Quantas pessoas vão ser cadastradas?\nSua opção: '))
for i in range(1, x+1):
    print('------{}ªPESSOA-----'.format(i))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [m/f]: ')).strip().lower()
    media+=idade
    if idade >= velho:
        velho = idade
        nomevelho = nome
    if sexo == 'f':
        numf+=1
    if sexo == 'm':
        numm+=1
print('\nA media das idades foi de: {:.2f}'.format(media/x))
print('A pessoa mais velha é {} e tem {} anos de idade.'.format(nomevelho, velho))
print('Se cadastraram {} homens e {} mulheres'.format(numm, numf))
