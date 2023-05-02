print('======Desafio 030======')
"""
Crie um programa que leia um número inteiro e mostre na tela se ele é ímpar ou par
"""

numero = int(input('Digite um número inteiro qualquer para descobrir se ele é ímpar ou par:'))
if numero % 2 == 0:
    print('O número {} é par!'.format(numero))
else:
    print('O número {} é ímpar'.format(numero))
