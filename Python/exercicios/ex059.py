print('======Desafio 059======')
"""
Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""

from time import sleep

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))

escolha = 0

while escolha != 5:
    print('='*22)
    print("""    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] FIM DO PROGRAMA""")
    
    escolha = int(input('Qual a sua opção: '))
    print('='*22)

    if escolha == 1:
        soma = valor1 + valor2
        print('{} + {} = {}'.format(valor1,valor2,soma))

    elif escolha == 2:
        multi = valor1 * valor2
        print('{} x {} = {}'.format(valor1,valor2,multi))
    
    elif escolha == 3:
        if valor1 > valor2:
            print('Entre {} e {} o maior valor é: {}'.format(valor1,valor2,valor1))
        elif valor1 < valor2:
            print('Entre {} e {} o maior valor é: {}'.format(valor1,valor2,valor2))
        elif valor1 == valor2:
            print('{} e {} são iguais'.format(valor1,valor2))
    
    elif escolha == 4:
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))

    elif escolha == 5:
        print('Finalizando programa...')
    else:
        print('OPÇÃO INVÁLIDA!')
    sleep(1)

print('\nFIM DO PROGRAMA')
