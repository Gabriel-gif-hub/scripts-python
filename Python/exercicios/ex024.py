print('======Desafio 024======')
"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome santo
"""

cidade = str(input('Digite o nome da sua cidade: ')).strip()
c1 = cidade.upper() 
separador = c1.split()
if 'SANTO' in separador[0]:
    print('A cidade {} começa com santo!'.format(cidade))
else:
    print('A cidade {} não começa com santo!'.format(cidade))
 