cores = {'clear': '\033[m',
         'azul': '\033[34m',
         'azulback': '\033[44m', }
print('{}======Desafio 008======{}'.format(cores['azul'], cores['clear']))
# Escreva um programa que leia um valor em metros e converta para centímetros e mílimitros
valor = float(input("Digite um valor em {}metros{}: ".format(
    cores['azul'], cores['clear'])))
centimetros = (valor*100)
millimetros = (valor*1000)
print('{}{}{} Metros equivalem a {}{:.2f}{} Centímetros e {}{:.2f}{} Milímetros'.format(
    cores['azulback'], valor, cores['clear'], cores['azulback'], centimetros, cores['clear'], cores['azulback'], millimetros, cores['clear']))
