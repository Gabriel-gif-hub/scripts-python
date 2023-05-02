print('======Desafio 051======')
"""
Desenvolva um programa que leia o primeiro termo e a razão de uma pa (progressão aritmética). No final, mostre os 10 primeiro termos dessa progressão.
"""
print('======= PROGRESSÃO ARITMÉTICA ======')
p_termo = int(input('Digite o PRIMEIRO TERMO da progressão aritmética: '))
razao = int(input('Digite a RAZÃO da progressão aritmética: '))
decimo = p_termo + (10) * razao
for c in range(p_termo,decimo,razao):
    print(c, end=' ->')
print('ACABOU')
