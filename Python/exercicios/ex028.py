print('======Desafio 028======')
"""
Escreva um programa que faça o computador "pensar" em um número int entre 0 e 5, e peça para o usuário descobrir qual foi o número escolhido pelo usuário.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
import random
import time
print('=='*20)
print('Eu duvido você adivinhar o número que eu pensar...')
print('=='*20)
x = random.randint(0,5)
numero = int(input('Digite um número entre 0 e 5: '))
print('Processando...')
time.sleep(1.5)
if  numero == x:
    print('Parabéns, você acertou!')
else:
    print('Eu pensei no número {}, tente novamente!'.format(x))
