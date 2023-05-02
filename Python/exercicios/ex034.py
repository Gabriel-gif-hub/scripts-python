print('======Desafio 034======')
"""
Escreva um programa que pergunte o salário da um funcionário e calcule o valor do seu aumento

Para salários superiores a R$1250.00 calcule um aumento de  10%

Para salários inferiores ou iguais, calcule 15%
"""
from time import sleep
salario = float(input('Digite o valor do seu salário para calcular o seu aumento: '))
if salario > 1250:
    aumento1 = (salario * 0.10) + salario
    print('Processando seu aumento...')
    sleep(1.5)
    print('Seu salário teve um aumento de 10%, saindo de R${:.2f} para R${:.2f}'.format(salario,aumento1))
else:
    aumento2 = (salario * 0.15) + salario
    print('Processando seu aumento...')
    sleep(1.5)
    print('Seu salário teve um aumento de 15%, saindo de R${:.2f} para R${:.2f}'.format(salario,aumento2))
