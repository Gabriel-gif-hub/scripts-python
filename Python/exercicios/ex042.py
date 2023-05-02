print('======Desafio 042======')
"""
Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: todos os lados iguais;
- Isóceles: dois lados iguais;
- Escaleno: todos os lados diferentes.
"""
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
cond1 = (r1+r2) > r3
cond2 = (r1+r3) > r2
cond3 = (r2+r3)> r1
if cond1 == True and cond2 == True and cond3 == True:
    if r1 == r2 == r3:
        print('É possível formar um triângulo EQUILÁTERO!')
    elif r1 == r2 or r1 == r2 or r2 == r3:
        print('É possível formar um triângilo ISÓCELES!')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('É possível formar um triângulo ESCALENO!')
else:
    print('Não é possível formar um triângulo com essas retas!')

