print('======Desafio 048======')
"""
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo entre 1 até 500
"""
s = 0
c = 0
for a in range(1,500+1):
    if a % 3 == 0 and a % 2 != 0:
        s += a
        c += 1
print('A soma de todos os {} números ímpares entre 1 e 500 é: {}'.format(c,s))





