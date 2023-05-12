print('======Desafio 072======')
"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso
"""
de_1_a_20 = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

opcoes = (0,1,2,3,4,5,6,7,8,9,10,11,1,13,14,15,16,17,18,19,20)

while True:

    while True:
        opcao = int(input('Digite um número entre 0 e 20: '))
        if 0 <= opcao <= 20:
            break
        print('Tente novamente',end=' ')

    print(f'Você digitou o número \033[35m{de_1_a_20[opcao]}\033[m')

    while True:
        conti = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
        if conti in 'NS':
            break

    if conti == 'N':
        break
print('Programa encerrado!')
