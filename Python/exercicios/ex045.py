print('======Desafio 045======')
"""
Crie um programa que faça o computador jogar um jokenpo com você
"""
from time import sleep
import random

lista = ['Pedra', 'Papel', 'Tesoura']
cpu = random.choice(lista)
print('====== FAÇA A SUA ESCOLHA ======')
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')
escolha = str(input('Qual a sua escolha? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)
if escolha == '1' and cpu == 'Pedra' or escolha == '2' and cpu == 'Papel' or escolha == '3' and cpu == 'Tesoura':
    print('\033[46mEMPATE\033[m')
    print('Ambos escolheram {}'.format(cpu))
elif escolha == '1' and cpu == 'Tesoura' or escolha == '2' and cpu == 'Pedra' or escolha == '3' and cpu == 'Papel':
    print('\033[42mVocê GANHOU\033[m!')
    print('Eu escolhi {}'.format(cpu))
elif escolha == '1' and cpu == 'Papel' or escolha == '2' and cpu == 'Tesoura' or escolha == '3' and cpu == 'Pedra':
    print('\033[41mVocê PERDEU!\033[m')
    print('Eu escolhi {}'.format(cpu))
else:
    print('Opção inválida!')
