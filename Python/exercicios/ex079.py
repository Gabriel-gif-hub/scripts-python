print('======Desafio 079======')
"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

lista = []
cont = 0

while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        cont += 1
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print(f'O valor {valor} não será adicionado pois já existe na lista!')
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print('='*30)
print(f'A lista possui {cont} elementos e essa é sua ordem de elementos em forma crescente:')
print(sorted(lista))
