print('======Desafio 026======')
"""
Faça um programa que leia uma frase pelo teclado e mostre:

Quantas vezes aparece a letra "A";
Em que posição ela aparece na primeira vez;
Em que posição ela aparce por último.
"""

frase = str(input('Digite uma frase motivacional de sua preferência: ')).strip()
f1 = frase.lower()
print('Na frase {}:'.format(frase.capitalize()))
print('A letra "A" aparece {} vezes!'.format(f1.count('a')+f1.count('ã')+f1.count('á')))
print('A letra "A" aparece na posição {} pela primera vez'.format(f1.find('a')+1))
print('A letra "A" aparece na posição {} pela última vez'.format(f1.rfind('a')+1))
