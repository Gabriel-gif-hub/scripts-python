print('======Desafio 065======')
"""
 Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

resposta = 'S'

media = soma = maior = menor = cont = 0

while resposta in 'S':
    numero = float(input('Digite um número: '))
    soma += numero
    cont += 1
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]

media = soma/cont

print('=='*22)
print('Você digitou {} valores e sua média foi {}'.format(cont,media))
print('O maior valor foi {} e o menor foi {}'.format(maior,menor))
