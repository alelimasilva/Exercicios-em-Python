'''Escreva um programa que leia a velocidade do carro
e caso ele passe de 80km/h ele sera multado em R$7,00
por cada km. '''

vel = float(input('Digite a velocidade do veiculo. '))
if vel <= 0:
    print('Velocidade Incorreta ou veiculo parado.')
elif vel <= 80:
    print('Velocidade permitida')
else:
    print('Velocidade proibida')
    multa = (vel-80) * 7
    print('Você recebeu uma multa de R${:.2f}'.format(multa))
