print('======Desafio 064======')
"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""

cont = n = s = 0

n = int(input('Digite uma valo [ 999 ] PARA O PROGRAMA: '))

while n != 999:
    cont += 1
    s += n
    n = int(input('Digite uma valo [ 999 ] PARA O PROGRAMA: '))

print('Você digitou {} valores, e soma deles é: {}'.format(cont,s))
