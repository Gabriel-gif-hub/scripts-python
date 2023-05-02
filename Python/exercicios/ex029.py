print('======Desafio 029======')
"""
Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80km/h, mostre uma mensagem que ele foi multado.

A multa vai custar R$7.00 por cada kmacimda do limite.
"""
velocidade = int(input('Digite a velocidade que o veículo estava: '))
if velocidade > 80:
    valor = (velocidade)-80
    multa = valor * 7
    print('Você foi multado num valor de R${}.00 por ultrapassar a velocidade máxima permitida!'.format(multa))
else:
    print('Você não foi multado!')
