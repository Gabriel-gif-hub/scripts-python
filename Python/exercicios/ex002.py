cores = {'clear': '\033[m',
         'purple': '\033[35m',
         'purpleback': '\033[45m'}

print('{}======DESAFIO 03======{}'.format(cores['purple'], cores['clear']))
print('{}Preencha as questões a seguir de acordo com suas informações: {}'.format(
    cores['purpleback'], cores['clear']))
dia = input('Em que {}DIA{} você nasceu? '.format(
    cores['purple'], cores['clear']))
mes = input('Em que {}MÊS{} você nasceu? '.format(
    cores['purple'], cores['clear']))
ano = input('Em que {}ANO{} você nasceu? '.format(
    cores['purple'], cores['clear']))
print('Você nasceu no dia {}{}{} de {}{}{} de {}{}{},correto?'.format(
    cores['purpleback'], dia, cores['clear'], cores['purpleback'], mes, cores['clear'], cores['purpleback'], ano, cores['clear']))
