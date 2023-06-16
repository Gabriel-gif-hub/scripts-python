print('======Desafio 078======')
"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
lista = []

for c in range(0,5):
    lista.append(int(input(f'Digite o valor da posição {c}: ')))

print('='*30)
print(f'O maior valor digitado foi: {max(lista)} Posições:',end=' ')
for p,c in enumerate(lista):
    if max(lista) == c:
        print(f'{p}...',end=' ')
print(f'\nO menor valor digitado foi: {min(lista)} Posições:',end=' ')
for p, c in enumerate(lista):
    if min(lista) == c:
        print(f'{p}...',end=' ')
