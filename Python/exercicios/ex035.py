print('======Desafio 035======')
"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário podem ou não formar um triângulo
"""
print('Digite a seguir os valores das retas para descobrir se é possível criar um triângulo com elas ou não:')
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
cond1 = (r1 + r2) > r3
cond2 = (r1 + r3) > r2
cond3 = (r2 + r3) > r1
if cond1 == True and cond2 == True and cond3 == True:
    print('Com as retas com os seguintes tamanhos:')
    print('{},{},{}'.format(r1,r2,r3))
    print('É possível criar um triângulo!')
else:
    print('Com os valores escolhidos:')
    print('{},{},{}'.format(r1,r2,r3))
    print('Não é possível criar um triângulo!')
