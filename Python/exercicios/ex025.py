print('======Desafio 025======')
"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem silva no nome
"""

nome = str(input('Digite o seu nome completo: ')).strip()
n1 = nome.upper()
if 'SILVA' in n1:
    print('O nome {} possui Silva'.format(nome.title()))
else:
    print('O nome {} não possui Silva'.format(nome.title()))
