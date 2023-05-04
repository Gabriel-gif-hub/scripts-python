print('======Desafio 067======')
"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

from time import sleep

while True:
    print('-'*30)
    numero = int(input('Digite o número que você deseja ver tabuada: '))
    if numero < 0:
        break
    for c in range(1,10+1):
        print(f'{numero} x {c} = {numero*c}')
    print('-'*30)

print('\nFINALIZANDO PROGRAMA [TABUADA]...')
sleep(1.5)
print('\n[TABUDADA] FINALIZADA')
