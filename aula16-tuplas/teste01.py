lanche = ('Hambúrguer','Suco','Pizza','Pudim')
# Tuplas sãi IMUTVEIS
# lanche[1] = 'água'(ESSE TIPO DE ALTERAÇÃO DARÁ ERRO)

# for c in lanche:
#     print(f'Eu vou comer {c}')

    
# for c in range(0,len(lanche)):
#     print(f'Vou comer {lanche[c]} na posição {c}')


for p,c in enumerate(lanche):
    print(f'Eu vou comer {c} na posição {p}')

print('\nComi demais!')

