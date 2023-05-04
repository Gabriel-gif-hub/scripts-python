print('======Desafio 070======')
"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
"""

total = acima_1000 = mais_barato = cont = 0
nome_mais_barato = ' ' 

while True:
    print('='*20)
    print('COMPRAS ONLINE')
    print('='*20)
    nome_produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1

    if preco > 1000:
        acima_1000 += 1
    
    if cont == 1 or preco < mais_barato:
        nome_mais_barato = nome_produto
        mais_barato = preco

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if continuar == 'N':
        break

print('='*30)
print(f"""Total gasto: R${total:.2f}
Produtos acima de R$1000: {acima_1000}
Produto mais barato: {nome_mais_barato} Custo: R${mais_barato:.2f}""")
