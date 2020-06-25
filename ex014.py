#0 Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

nome = str(input('Digite o nome da cidade: ')).strip()
nome = nome.lower()
print(nome[:5] == 'santo')