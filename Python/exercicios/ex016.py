print('======Desafio 016======')
# Crie um programa que leia um número Real qualquer pelo teclado, e mostre na tela a sua porção inteira

# Ex: digite um número = 3.127
# O número 3.127 tem a parte inteira 3

import math
numero = float(input('Digite um número real qualquer: '))
parte_inteira = math.trunc(numero)
print('A parte inteira do número {} é {}'.format(numero,parte_inteira))
