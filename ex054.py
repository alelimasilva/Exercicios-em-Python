''' Faça um programa que tenha uma função chamada notas() que pode receber
    várias notas de alunos e vai retornar um dicionário com as seguintes
    informações:
        - Quantidade de notas
        - A maior nota
        - A menor nota
        - A média da turma
        - A situação (opcional)
        Adicione também as docstrings da função. '''

def notas_aluno(*nota, situacao=False):
    """
    Função para analisar as notas e a siituação de um aluno.
    :param nota: Recebe uma ou varias notas do aluno
    :param situacao: Analisa a situação da media do aluno(opcional)
    :return: Retorna um dicionario com as informações do aluno
    """
    info_alunos = dict(total=len(nota), maior=max(nota), menor=min(nota), media=sum(nota) / len(nota))
    if situacao:
        if info_alunos['media'] < 5:
            info_alunos['situacao'] = 'RUIM'
        elif info_alunos['media'] < 7:
            info_alunos['situacao'] = 'RAZOÁVEL'
        elif info_alunos['media'] < 10:
            info_alunos['situacao'] = 'ÓTIMO'
    return info_alunos


# chamada
resp = notas_aluno(5.5, 9.5, 10, 6.5, situacao=True)
print(f'Dicionário de dados: {resp}')
print()
help(notas_aluno)
