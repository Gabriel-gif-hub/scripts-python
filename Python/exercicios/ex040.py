print('======Desafio 040======')
"""
Crie um programa que leia duas notas de um aluno  e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida.

- Média abaixo de 5.0 = reprovado
- Média entre 5.0 e 6.9 = recuperação
- Média 7.0 ou superior = aprovado
"""
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
media = (n1+n2)/2
print('Sua média foi {}'.format(media))
if media < 5.0:
    print('Você está REPROVADO!')
elif media >= 5.0 and media < 7.0:
    print('Você está de RECUPERAÇÃO!')
elif media >= 7.0:
    print('Você está APROVADO!')
