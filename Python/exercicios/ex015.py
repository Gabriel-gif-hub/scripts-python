print('======Desafio 015======')
# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado, e a
# quantidade de dias que o mesmo foi alugado. Em seguida calcule o preço a se pagar.

# Custo: R$60,00 por dia e R$0,15 por KM rodado

dias = int(input('Digite a quantidade de dias que esteve com o automóvel: '))
km = float(input('Digite quantos KM foram percorridos com o automóvel: '))
custo1 = (dias*60)
custo2 = (km*0.15)
custototal = (custo1+custo2)
print('Considerando que o Veículo percorreu {:.2f} KM por {} Dias...'.format(km,dias))
print('Seu aluguel ficou em R${:.2f}'.format(custototal))
