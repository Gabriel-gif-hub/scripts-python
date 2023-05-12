print('======Desafio 073======')
"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time do Corinthians.
"""
tabela = ('Botafogo', 'Palmeiras', 'Cruzeiro', 'Fortaleza', 'São Paulo', 'Fluminense', 'Grêmio', 'Internacional', 'Bahia', 'Athletico-PR',
          'Vasco', 'Bragantino', 'Cuiabá','Santos', 'Atlético-MG', 'Flamengo', 'Corinthians', 'Goiás', 'Coritiba', 'América-MG')

ordem = sorted(tabela)

print('='*30)

print('\033[33mTabela Atual\033[m:')
cont = 1
for a in tabela:
    print(f'{cont}º{a}')
    cont += 1

print(f'\n\033[32mOs 5 primeiros colocados são\033[m: \n1º-{tabela[0]}\n2º-{tabela[1]} \n3º-{tabela[2]} \n4º-{tabela[3]} \n5º-{tabela[4]}')

print(f'\n\033[31mOs 4 últimos colocados são\033[m: \n17º-{tabela[-4]}\n18º-{tabela[-3]}\n19º-{tabela[-2]}\n20º-{tabela[-1]}')

print('\n\033[35mTimes em ordem alfabética\033[m:\n')
for c in ordem:
    print(c)

pro = tabela.index('Corinthians')

print(f'\n\033[36mO {tabela[-4]} está na posição\033[m: \n{pro+1}ª')




