print('======Desafio 046======')
"""
Faça um programa que mostre na tela um contagem q regressiva para o estouro de fogos de artifício, sendo de 0 a 10, com pausa de 1 segundo entre eles:
"""

from time import sleep

print('CONTAGEM REGRESSIVA PARA OS FOGOS')
for t in range(10,-1,-1):
    print(t)
    sleep(1)
print('Caboooom!')
