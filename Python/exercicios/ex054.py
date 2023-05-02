print('======Desafio 054======')
"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioiridade e quantas já são maiores.

- Utilizar a maioridade como 21 anos.
"""
from datetime import date
tot_maior = 0
tot_menor = 0
for c in range(1,7+1):
    nascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = date.today().year - nascimento
    if idade >= 21:
        tot_maior += 1
    else:
        tot_menor += 1
print('\n{} das {} pessoas mencionadas SÃO MAIORES de idade!'.format(tot_maior,tot_maior+tot_menor))
print('{} das {} pessoas mencionadas SÃO MENORES de idade!'.format(tot_menor,tot_maior+tot_menor))
