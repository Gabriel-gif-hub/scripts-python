print('======DESAFIO 002======')
nome = input('Digite o seu nome: ')
cores = {'clear': '\033[m',
         'blue': '\033[34m'}
print('É um prazer te conhecer, {}{}{}'.format(
    cores['blue'], nome, cores['clear']))
