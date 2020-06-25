''' Crie um programa que tenha uma função chamada voto() que vai receber
    como parâmetro o ano de nascimento de uma pessoa, retornando um valor
    literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO
    nas eleições.'''

def calcidade(ano):
    from datetime import date
    idade = date.today().year - ano
    return idade

def voto(idade):
    if idade < 18:
        return 'Negado'
    elif idade < 65:
        return 'Obrigatório'
    else:
        return 'Opcional'


ano = int(input('Informe o ano de nascimento: '))
print(f'Com {calcidade(ano)} anos. Voto {voto(calcidade(ano))}')
