v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
soma = v1 + v2
cores = {'clear' : '\033[m',
         'red' : '\033[31m',
         'redsub' : '\033[41m',
         'purple' : '\033[35m',
         'purplesub' : '\033[45m'
         }
print('A soma dos valores {}{}{} e {}{}{} é {}{}{}'.format(cores['red'],v1,cores['clear'],cores['red'],v2,cores['clear'],cores['redsub'],soma,cores['clear']))
