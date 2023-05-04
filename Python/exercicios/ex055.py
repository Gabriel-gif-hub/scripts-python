print('======Desafio 055======')
"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e menor peso lido.
"""
maior = 0
menor = 0
for c in range(1,5+1):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}kg'.format(maior))
print('O menor peso lido foi {}kg'.format(menor))

