jogador = list()
jogador.append('Neymar')
jogador.append(31)
elenco = list()
elenco.append(jogador[:])
jogador[0] = 'Messi'
jogador[1] = 35
elenco.append(jogador[:])
print(elenco)
