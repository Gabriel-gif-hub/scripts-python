print('======Desafio 080======')
"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""
lista = []
for c in range(0,5):
    valor = int(input(f'Digite o {c+1}º número: '))
    if c == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Valor adicionado na útima posição...')
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f'Valor adicionado na posição {pos}...')
                break
            pos += 1

print('='*30)
print(f'Lista ordenada: {lista}')
