print('======Desafio 049======')
"""
Refaçao desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o for.
"""
numero = int(input('Digite um número para ver sua tabuada: '))
for c in range(1,10+1):
    print('{} x {} = {}'.format(numero,c,numero*c))
