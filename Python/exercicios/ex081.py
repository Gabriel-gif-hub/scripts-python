print('======Desafio 081======')
"""
Crie um programa que vai ler vários números e colocar em uma lista.    

Depois disso mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = []

cont1 = tot = 0

while True:

    valor = int(input(f'Digite o {cont1+1}º valor: '))
    cont1 += 1

    if valor not in lista:
        lista.append(valor)
        tot += 1
    else:
        print(f'O valor {valor} não foi adicionado pois já existe na lista...')

    print('='*30)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]?' )).upper().strip()[0]
    if continuar == 'N':
        break


print(f'Você digitou {tot} valores')

lista.sort(reverse=True)

print(f'A lista em ordem decrecente é: {lista}')

if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
