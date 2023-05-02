print('======Desafio 018======')
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

angulo = int(input('Digite o valor de um ângulo qualquer: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('Os valores do Ângulo {}:'.format(angulo))
print('Seno: {:.2f} cm'.format(seno))
print('Cosseno: {:.2f} cm'.format(cosseno))
print('Tangente: {:.2f} cm'.format(tangente))
