print('======Desafio 074======')
"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
from random import randint

numero = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))


print('Os números sorteados foram: ',end='')
for c in numero:
    print(f'{c}',end=' ')

print(f'\n\nO maior número sorteado foi: {max(numero)}')
print(f'O menor número sorteado foi: {min(numero)}')

