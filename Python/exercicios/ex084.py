print('======Desafio 084======')
"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final,mostre:

A) Quantas pessoas foram cadastradas.                                                                       
B) Uma listagem com as pessoas mais pesadas.                                                       

C) Uma listagem com as pessoas mais leves.
"""
# Variáveis simples
maior = menor = 0

# Listas
pessoas = list()
individuo = list()

# Laço
while True:
    individuo.append(str(input('Nome: ').strip().title()))
    individuo.append(float(input('Peso: ').strip()))
    if len(pessoas) == 0:
        maior = menor = individuo[1]
    else:
        if individuo[1] > maior:
            maior = individuo[1]
        if individuo[1] < menor:
            menor = individuo[1]
    pessoas.append(individuo[:])
    individuo.clear()

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break

# Terminal
print('='*30)
print(f'{len(pessoas)} pessoas foram cadastradas')
print(f'O maior peso foi de {maior}Kg! Peso de: ',end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]',end='')

print()
print(f'O menor peso foi de {menor}Kg! Peso de: ',end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]',end='')
