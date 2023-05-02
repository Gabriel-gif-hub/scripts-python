print('======Desafio 036======')
"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal sabendo que ele não pode exceder 30% do salário ou então o empréstimo será negado.
"""
print('CÁLCULO DE EMPRÉSTIMO BANCÁRIO')
valor_casa = float(input('Digite o valor para empréstimo que deseja adiquirir: R$'))
salario = float(input('Agora informe o valor de seu salário (mensal): R$'))
anos = int(input('Digite em quantos anos deseja pagar o empréstimo: '))
prestacao = valor_casa/(anos*12)
if prestacao < (salario*0.3):
    print('Para um empréstimo de R${} com uma prestação de R${:.2f} durante {} anos'.format(valor_casa,prestacao,anos))
    print('De acordo com nossas regras, você pode realizar o empréstimo conosco!')

else:
    print('Para um empréstimo de R${} com uma prestação de R${:.2f} durante {} anos'.format(valor_casa,prestacao,anos))
    print('De acordo com nossas regras seu empréstimo foi negado!')

