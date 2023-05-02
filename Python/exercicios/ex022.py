print('======Desafio 022======')
"""
Crie um programa que leia o nome compleo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas;
- Todas as minúsculas;
- Quantas letras no total (sem considerar os espaços);
- Quantas letras tem o primeiro nome.

"""

nome = str(input('Digite o seu nome completo: ')).strip()
print('Seu nome em letras Maiúculas é: {}'.format(nome.upper()))
print('Seu nome em letras Minúsculas é: {}'.format(nome.lower()))
print('Seu nome possui {} letras no total !'.format(len(nome)-nome.count(' ')))
separator = nome.split()
print('Seu primeiro nome {} possui {} letras'.format(separator[0], len(separator[0])))