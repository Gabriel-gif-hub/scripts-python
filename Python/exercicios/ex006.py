cores = {'clear': '\033[m',
         'yellow': '\033[33m',
         'yellowback': '\033[43m'}
print('{}======Desafio 006======{}'.format(cores['yellow'], cores['clear']))
# Crie um programa que leia um número e mostre seu dobro, triplo e raiz quadrada
n = int(input('Digite um {}número{} para descobrir seu {}dobro{}, {}triplo{} e {}raiz quadrada{}:'.format(
    cores['yellow'], cores['clear'], cores['yellow'], cores['clear'], cores['yellow'], cores['clear'], cores['yellow'], cores['clear'])))
d = (n*2)
t = (n*3)
r = (n**(1/2))
print('Os valores correspondentes ao número informado são:\n {}Dobro{} {}{}{}\n {}Triplo{} {}{}{}\n {}Raiz Quadrada{} {}{:.2f}{}'.format(
    cores['yellow'], cores['clear'], cores['yellowback'], d, cores['clear'], cores['yellow'], cores['clear'], cores['yellowback'], t, cores['clear'], cores['yellow'], cores['clear'], cores['yellowback'], r, cores['clear']))
