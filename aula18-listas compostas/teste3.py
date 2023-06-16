# Contadores
totmai = totmen = 0

# Listas
elenco = list()
dado = list()

# Cores
cores = [['limpa','\033[m'],['vermelho','\033[31m'],['verde','\033[33m']]

# Laço com o prenchimento do usuário para cada nome e idade
for c in range(0,3):
    dado.append(str(input('Nome: ').title()))
    dado.append(int(input('Idade: ')))
    elenco.append(dado [:])
    dado.clear()

# Condição de maioridade para cada pessoa da lista elenco
for p in elenco:
    if p[1] > 18:
        print(f'{p[0]} tem {p[1]} anos, logo,{cores[2][1]} é maior de idade{cores[0][1]}!')
        totmai += 1
    else:
        print(f'{p[0]} tem {p[1]} anos, logo, {cores[1][1]}não é maior de idade{cores[0][1]}!')
        totmen += 1

print(f'Temos {cores[2][1]}{totmai} maiores de idade{cores[0][1]} e {cores[1][1]}{totmen} menores de idades{cores[0][1]}!')
