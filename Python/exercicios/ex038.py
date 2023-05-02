print('======Desafio 038======')
"""
Escreva um programa que leia dois número inteiros e compare-os, mostrando na tela uma mensagem.

- O primeiro valor é maior; 
- O segundo valor é  maior;
- Os dois valores são iguais.
"""

print('DIGITE NÚMERO INTEIROS PARA COMPARAÇÃO')
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print('O PRIMEIRO valor é o MAIOR! ')
elif n1 < n2:
    print('O SEGUNDO valor é o MAIOR!')
elif n1 == n2:
    print('Os DOIS valores são IGUAIS!')
