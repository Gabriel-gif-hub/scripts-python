cores = {'clear': '\033[m',
         'green': '\033[32m',
         'greenback': '\033[42m'}
print('{}======Desafio 005======{}'.format(cores['green'], cores['clear']))
# Faça um programa que leia um número inteiro e mostre seu sucessor e antecessor
n = int(input('Digite um {}número{}:'.format(cores['green'], cores['clear'])))
s = (n+1)
a = (n-1)
print('Seu {}sucessor{} é: {}{}{}'.format(
    cores['green'], cores['clear'], cores['greenback'], s, cores['clear']))
print('Seu {}antecessor{} é: {}{}{}'.format(
    cores['green'], cores['clear'], cores['greenback'], a, cores['clear']))
