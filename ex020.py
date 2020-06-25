'''  Escreva um programa para aprovar um emprestimo
para a  compra de uma casa o programa precisa do:
 salario
 valor da casa
 tempo desejado para a compra(em anos)
Calcule o valor da prestação mensal sendo que ela não pode
passar 30% do salario.'''

casa = float(input('Qual o valor da casa? R$: '))
salario = float(input('Qual o seu salario? R$: '))
ano = int(input('Em quantos anos deseja pagar a casa? '))

ano = ano * 12
valor = casa / ano
if valor > (salario / 10) * 3:
    print('Sua prestação foi negada.\nPois ela excede 30% do seu salario')
else:
    print('Prestação aprovada.\nNo valor de {:.2f}'.format(valor))
