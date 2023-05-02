print('======Desafio 037======')
"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher a qaul será a base da conversão:

- 1 para BINÁRIO
- 2 para OCTAL
- 3 para HEXADECIMAL
"""
# fazendo o usuário digitar o número

numero = int(input('Digite um número inteiro que você deseja converter: '))
# criando tabela para escolha
print('ESCOLHA UMA DAS OPÇÕES ABAIXO:')
print(' [ 1 ] = CONVERSÃO PARA BINÁRIO')
print(' [ 2 ] = CONVERSÃO PARA OCTAL')
print(' [ 3 ] = CONVERSÃO PARA HEXADECIMAL')

opcao = int(input('OPÇÃO: '))
# opção para o usuário

# condição de escolha
# o format (numero, 'b ou o ou x') faz o python transformat automaticamente na base desejada
if opcao == 1:
    binario = format(numero, 'b')
    print('{} convertido em BINÁRIO é: {}'.format(numero, binario))
elif opcao == 2:
    octal = format(numero, 'o')
    print('{} convertido em OCTAL é: {}'.format(numero, octal))
elif opcao == 3:
    hexadecimal = format(numero, 'x')
    print('{} convertido em HEXADECIMAL é: {}'.format(numero, hexadecimal))
else:
    print('Opção inválida')
