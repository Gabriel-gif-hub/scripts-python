cores = {'clear': '\033[m',
         'red': '\033[31m',
         'redback': '\033[1;41m'}
print('{}======DESAFIO 005======{}'.format(cores['red'], cores['clear']))
a = input('Digite algum {}valor{} para a especificação do mesmo: '.format(
    cores['red'], cores['clear']))
print('O tipo primitivo de {}{}{} é {}{}{}'.format(
    cores['red'], a, cores['clear'], cores['redback'], type(a), cores['clear']))
print('{}{}{} é um numeral e alfabético: {}{}{}'.format(
    cores['red'], a, cores['clear'], cores['redback'], a.isalnum(), cores['clear']))
print('{}{}{} é alfabético: {}{}{}'.format(
    cores['red'], a, cores['clear'], cores['redback'], a.isalpha(), cores['clear']))
print('{}{}{} é decimal: {}{}{}'.format(
    cores['red'], a, cores['clear'], cores['redback'], a.isdecimal(), cores['clear']))
print('{}{}{} é um espaço: {}{}{}'.format(
    cores['red'], a, cores['clear'], cores['redback'], a.isspace(), cores['clear']))
print('{}{}{} é minúscula: {}{}{}'.format(
    cores['red'], a, cores['clear'], cores['redback'], a.islower(), cores['clear']))
print('{}{}{} é maiúsculo: {}{}{}'.format(
    cores['red'], a, cores['clear'], cores['redback'], a.isupper(), cores['clear']))
print('{}{}{} é um dígito: {}{}{}'.format(
    cores['red'], a, cores['clear'], cores['redback'], a.isdigit(), cores['clear']))
