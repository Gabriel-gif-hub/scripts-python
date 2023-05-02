print('======Desafio 058======')
"""
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
from random import randint
from time import sleep

print('='*22)
print('SEJA BEM VINDO(A)')
print('='*22)
print('\nSERÁ QUE CONSEGUE ME SUPERAR E ADIVINHAR O NÚMERO QUE ESTOU PENSANDO?')
sleep(1)
print('DICA: ELE ESTÁ ENTRE \033[45m0\033[m E \033[045m10\033[m')
sleep(1)

x = randint(0,10)
quantidade = 0
acertou = False

while not acertou:
    palpite = int(input('Digite o seu palpite: '))
    quantidade += 1
    if palpite == x:
        acertou = True
    else:
        if palpite > x:
            print('Mais para BAIXO')
        elif palpite < x:
            print('Mais para CIMA')

if quantidade > 1:
    print('Você precisou de {} tentativas!\n\nMas acertou, PARABÉNS!'.format(quantidade))
else:
    print('Você acertou de primeira!\n\nPARABÉNS!')
