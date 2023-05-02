cores = {'clear': '\033[m',
         'green': '\033[32m',
         'greenback': '\033[1;42m'}
print('{}======DESAFIO 04======{}'.format(cores['green'], cores['clear']))
print('Digite o que as questões a seguir pedirem para {}somar{} dois números:'.format(
    cores['green'], cores['clear']))
n1 = int(input('Digite o {}primeiro{} número: '.format(
    cores['green'], cores['clear'])))
n2 = int(input('Digite o {}segundo{} número: '.format(
    cores['green'], cores['clear'])))
soma = (n1) + (n2)
print('O resultado da soma de {}{}{} e {}{}{} é {}{}{}'.format(
    cores['green'], n1, cores['clear'], cores['green'], n2, cores['clear'], cores['greenback'], soma, cores['clear']))
