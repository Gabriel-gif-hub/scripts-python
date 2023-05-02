print('======Desafio 019======')
'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro , faça um programa q ue  a jude  ele, lendo o nome deles  e 
escrevendo o nome do escolhido
'''
import random
nome1 = str(input('Digite o nome do primeiro aluno: '))
nome2 = str(input('Digite o nome do segundo aluno: '))
nome3 = str(input('Digite o nome do terceiro aluno: '))
nome4 = str(input('Digite o nome do quarto aluno: '))
lista_de_alunos = [nome1,nome2,nome3,nome4]
escolha_aleatoria = random.choice(lista_de_alunos)
print('O aluno escolhido para limpar o quadro foi o/a {}!'.format(escolha_aleatoria))
