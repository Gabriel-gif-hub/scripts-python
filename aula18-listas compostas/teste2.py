# Criando a lista composta
elenco = [['Gabriel',20],['Neymar',31],['Messi',35]]

# cores
v = '\033[31m'
a = '\033[33m'
l = '\033[m'
# Apresentando a lista no terminal de forma organizada
for p in elenco:
    print(f'O {v}{p[0]}{l} tem {a}{p[1]}{l} anos de idade!')
