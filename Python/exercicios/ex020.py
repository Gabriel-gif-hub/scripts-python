print('======Desafio 020======')
'''
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o 
nome dos quatro alunos e mostre a ordem sorteada
'''
import random

nome1 = str(input('Digite o nome do/a primeiro/a aluno/a: '))
nome2 = str(input('Digite o nome do/a segundo/a aluno/a: '))
nome3 = str(input('Digite o nome do/a terceiro/a aluno/a: '))
nome4 = str(input('Digite o nome do/a quarto/a aluno/a: '))
lista = [nome1,nome2,nome3,nome4]
ordem = random.sample(lista, 4)
print('A ordem da apresentação do trabalho será {}'.format(ordem))
