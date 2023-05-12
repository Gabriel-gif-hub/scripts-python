print('======Desafio 076======')
"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""
listagem = ('Água', 3.00,
            'Creatina',75.00,
            'Whey Protein',98.00,
            'Cafeína',54.00,
            'Glutamina',45.00,
            'Pré-treino',110.00,
            'Barra de cereal',3.50)

print('Lista de produtos: ')
print('='*40)
for c in range(0,len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<30}',end='')
    else:
        print(f'R${listagem[c]:>7.2f}')
print('='*40)
