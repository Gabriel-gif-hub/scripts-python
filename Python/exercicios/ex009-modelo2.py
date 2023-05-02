cores = {'clear': '\033[m',
         'purple': '\033[35m',
         'purpleback': '\033[45m'}
print('{}======Desafio 009======{}'.format(cores['purple'], cores['clear']))
# Faça um programa que leia um número inteiro e mostre na tela a sua tabuada]
valor = int(input('Digite um {}número inteiro{} para ver sua {}tabuada{}: '.format(
    cores['purple'], cores['clear'], cores['purple'], cores['clear'])))
print('{} x {} = {}{}{}'.format(
    valor, 1, cores['purpleback'], valor*1, cores['clear']))
print('{} x {} = {}{}{}'.format(
    valor, 2, cores['purpleback'], valor*2, cores['clear']))
print('{} x {} = {}{}{}'.format(
    valor, 3, cores['purpleback'], valor*3, cores['clear']))
print('{} x {} = {}{}{}'.format(
    valor, 4, cores['purpleback'], valor*4, cores['clear']))
print('{} x {} = {}{}{}'.format(
    valor, 5, cores['purpleback'], valor*5, cores['clear']))
print('{} x {} = {}{}{}'.format(
    valor, 6, cores['purpleback'], valor*6, cores['clear']))
print('{} x {} = {}{}{}'.format(
    valor, 7, cores['purpleback'], valor*7, cores['clear']))
print('{} x {} = {}{}{}'.format(
    valor, 8, cores['purpleback'], valor*8, cores['clear']))
print('{} x {} = {}{}{}'.format(
    valor, 9, cores['purpleback'], valor*9, cores['clear']))
print('{} x {} = {}{}{}'.format(
    valor, 10, cores['purpleback'], valor*10, cores['clear']))
