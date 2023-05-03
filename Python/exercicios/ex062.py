print('======Desafio 062======')
"""
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
"""

p_termo = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão da PA: '))
termo = p_termo
cont = 1
total = 0
mais = 10

print('Calculando...\n',end='')

while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo),end='')
        termo += razao
        cont += 1
    print('PAUSA',end='')
    mais = int(input('\nDeseja vizualizar mais quantos termos? '))
print('PA finalizada com {} termos'.format(total))
