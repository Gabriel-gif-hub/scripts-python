print('======Desafio 068======')
"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

from random import randint

cont = 0

while True:
    print('='*30)
    n_pc = randint (0,10)
    n_usuario = int(input('Digite um número: '))
    total = n_pc + n_usuario
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('Par ou Ímpar [P/I]? ')).upper().strip()[0]
    print(f'O computador escolheu: {n_pc}\nE você: {n_usuario}\nTotal: {total}')
    print('\033[33mDEU PAR\033[m' if total % 2 == 0 else '\033[35mDEU ÍMPAR\033[m')
    if opcao == 'P':
        if total % 2 == 0:
            print('\033[32mVocê VENCEU!\033[m')
            cont += 1
        else:
            print('\033[31mVocê PERDEU!\033[m')
            break

    if opcao == 'I':
        if total % 2 == 1:
            print('\033[32mVocê VENCEU!\033[m')
            cont += 1
        else:
            print('\033[31mVocê PERDEU!\033[m')
            break

    print('='*30)
    print('Droga eu perdi! Vamos de novo!')

print(f'GAME OVER\nTotal de vitórias: {cont}')
