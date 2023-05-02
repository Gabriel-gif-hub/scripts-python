print('======Desafio 017======')
# Faça um programa que leia o comprimento do cateto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento
# da hipotenusa.
import math
cateto = float(input('Digite o comprimento do cateto do triângulo retângulo: '))
cateto_adjacente = float(input('Agora digite o cateto ajacente do triângulo retângulo: '))
hipotenusa = math.hypot(cateto,cateto_adjacente)
print('O valor da hipotenusa do triângulo retângulo com os seguintes dados:')
print('Cateto {} cm'.format(cateto))
print('Cateto Adjacente {} cm'.format(cateto_adjacente))
print('Possui a Hipotenusa com {:.2f} cm'.format(hipotenusa))
