print('======Desafio 023======')
"""
Faça um programa que leia um número de 0 a  9999 e mostre cada um dos dígitos separados
"""
numero = int(input('Digite um valor entre 0 e 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('O número {} equivale a:'.format(numero))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
