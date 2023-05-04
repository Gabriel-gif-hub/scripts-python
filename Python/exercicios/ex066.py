print('======Desafio 066======')
"""
Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
"""

soma = cont = 0

while True:
    numero = int(input('Digite um número [999 Para o programa]: '))
    if numero == 999:
        break
    soma += numero
    cont+=1

print('=='*25)
print(f'\nVocê digitou {cont} números e sua soma foi {soma}')
