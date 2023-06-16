print('======Desafio 082======')
"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""
# Declarando listas
lista = []
l_par= []
l_impar = []

# Laço com escolha de continuação
while True:
    numero = int(input('Digite um número: '))

    if numero not in lista:
        lista.append(numero)

        # Condição para pares ou ímpares
        if numero % 2 == 0:
            l_par.append(numero)
        else:
            l_impar.append(numero)
    else:
        print(f'O número {numero} não será adicionado pois já existe na lista!')

    # Laço de escolha para continuar
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if continuar == 'N':
        break

# Lista organizadas

lista.sort()
l_par.sort()
l_impar.sort()

# Terminal

print('='*30)
print(f'''Lista completa: {lista}
Lista de pares: {l_par}
Lista de ímpares: {l_impar}''')
