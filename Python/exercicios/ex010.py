cores = {'clear': '\033[m',
         'ciano': '\033[36m',
         'cianoback': '\033[46m'}
print('{}======Desafio 010======{}'.format(cores['ciano'], cores['clear']))
# Crie um programa que lê quanto dinheiro uma pessoa tem na carteira e
# mostre quantos Dólares ela pode comprar

# Valor do dólar (13/03/2023) = R$5,24

real = float(input('Digite quantos {}reais{} você deseja converter em {}dólares{}: '.format(
    cores['ciano'], cores['clear'], cores['ciano'], cores['clear'])))
dolar = (real/5.24)
print('Seus {}R${:.2f}{} equivalem a {}USS${:.2f}{}'.format(
    cores['cianoback'], real, cores['clear'], cores['cianoback'], dolar, cores['clear']))
