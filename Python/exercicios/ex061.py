print('======Desafio 061======')
"""
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
# from time import sleep

# p_termo = int(input('Digite o primeiro termo da PA: '))
# razao = int(input('Digite a razão da PA: '))
# c = p_termo
# decimo = p_termo + (10) * razao

# print('='*22)
# print('Calculando...\n\nPA: ',end='')
# sleep(1.5)

# while c != decimo:

#     print('{} '.format(c),end='')
#     c += razao

from time import sleep

p_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
termo = p_termo
cont = 1

print('Calculando...\n',end='')

while cont <=10:
    print('{} -> '.format(termo),end='')
    termo += razao
    cont += 1

print('FIM',end='')
