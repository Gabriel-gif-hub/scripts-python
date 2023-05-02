cores = {'clear': '\033[m',
         'grey': '\033[1;37m',
         'greyback': '\033[47m'}
print('======Desafio 011======')
# Faça um programa que leia a altura e largura de um parede em metros , calcule a sua área e a
# quantidade de tinta necessária para pintá-la.

# Cada litro de tinta pinta uma área = 2m*2

altura = float(input('Digite a {}altura{} da parede: '.format(
    cores['grey'], cores['clear'])))
largura = float(input('Digite a {}largura{} da parede: '.format(
    cores['grey'], cores['clear'])))
area = (altura*largura)
litros = (area/2)
print('Para uma parede com {}{} M²{} é necessário {}{} Litros{} de Tinta'.format(
    cores['greyback'], area, cores['clear'], cores['greyback'], litros, cores['clear']))
