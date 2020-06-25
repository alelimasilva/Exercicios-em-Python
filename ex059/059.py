''' Adicione ao módulo moeda.py criado nos desafios anteriores, uma função
    chamada resumo(). que mostre na tela algumas informações geradas pelas
    funções que já temos no módulo criado até aqui.
    E adicione um validadore de dados para aceitar apenas valores monetarios.'''

from ex059 import dados

valor = dados.leianum('Digite o preço: R$')
porcento = dados.leianum('Digite a porcentagem: ')
dados.resumo(valor, porcento)
