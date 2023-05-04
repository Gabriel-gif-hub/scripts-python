print('======Desafio 071======')
"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

print('='*20)
print('BANCO MAIS VOCÊ')
print('='*20)
valor = int(input('Qual valor você deseja sacar: R$'))
saque = valor

nota_50 = nota_20 = nota_10 = nota_1 = 0

while True:
    if saque >= 50:
        saque - 50
        nota_50 += 1
    if saque >= 20 and saque < 50:
        saque -20
        nota_20 += 1
    if saque >= 10 and saque < 20:
        saque - 10
        nota_10 += 1
    if saque >= 1 and saque < 10:
        saque - 1
        nota_1 += 1
    if saque == 0:
        break
    
print(f"""Você receberá:
{nota_50} notas de R$50
{nota_20} notas de R$20
{nota_10} notas de R$10
{nota_1} notas de R$1""")
