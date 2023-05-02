print('======Desafio 052======')
"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

- Números primos são aqueles divisíveis apenas por 1 e por eles mesmos.
"""
numero = int(input('Digite um número inteiro: '))
cont = 0
for c in range(1,numero+1):
    if numero % c == 0:
        cont += 1
        print('\033[44m',end= ' ')
    else:
        print('\033[41m',end= ' ')
    print(c, end=' ')
if cont == 2:
    print('\033[m\nO número {} É PRIMO!'.format(numero))
    print('Pois é divisível somente por 1 e ele mesmo!')
else:
    print('\033[m\nO número {} NÃO É PRIMO!'.format(numero))
    print('Pois ele não é divísivel somente por 1 e ele mesmo!')
