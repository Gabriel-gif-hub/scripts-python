cores = {'clear': '\033[m',
         'yellow': '\033[33m',
         'yellowback': '\033[43m'}
print('{}======Desafio 007======{}'.format(cores['yellow'], cores['clear']))
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média
n1 = float(input('Digite a sua {}primeira{} nota:'.format(cores['yellow'], cores['clear'])))
n2 = float(input('Digite a sua {}segunda{} nota:'.format(
    cores['yellow'], cores['clear'])))
media = (n1+n2)/2
print('Sua média foi: {}{:.1f}{}'.format(
    cores['yellowback'], media, cores['clear']))
