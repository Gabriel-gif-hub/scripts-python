print('======Desafio 041======')
"""
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 25 anos: Sênior
- Acima de 25 anos: Master 
"""

from datetime import date

ano = int(input('Digite o ano de seu nascimento: '))
ano_atual = date.today().year
idade = int(ano_atual) - ano
print('Idade: {} anos'.format(idade))
if idade <=9:
    print('Categoria: MIRIM')
elif idade > 9 and idade <= 14:
    print('Categoria: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Categoria: JUNIOR')
elif idade > 19 and idade <=25:
    print('Categoria: SÊNIOR')
elif idade > 25:
    print('Categoria: MASTER')
