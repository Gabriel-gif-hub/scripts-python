print('======Desafio 031======')
"""
Desenvolva um programa que pergunte a distância de um a viagem em km.

Calcule o preço da passagem, cobrando R$0.50 por km para viagens de até 200km.

Cobre R$0,45 para viagens mais longas
"""
km = float(input('Digite a quantidade de kms de sua viagem: '))
if km <= 200:
    valor1 = (km*0.50)
    print('O valor da sua viagem de {} km é de: R${}'.format(km,valor1))
else:
    valor2 = (km*0.45)
    print('O valor da sua viagem de {} km é de: R${}'.format(km,valor2))

