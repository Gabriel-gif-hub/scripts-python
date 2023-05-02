print('======Desafio 050======')
"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar desconsidere-o.
"""
s = 0
c = 0
for a in range(1,6+1):
    numero = int(input('Digite o {}ª número: '.format(a)))
    if numero % 2 == 0:
        s += numero
        c += 1
if c > 1:
    print('A soma dos {} número pares é: {}'.format(c,s))
else:
    print('Só existe um número par!')

