print('======Desafio 075======')
"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
"""
numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')),)

print(f'Você digitou os valores: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu primeiro na posição {numeros.index(3)+1}')
else:
    print('O número 3 não apareceu em nenhuma posição!')

print('Os números pares são: ',end='')
for n in numeros:
    if n % 2 == 0:
        print(n,end=' ')
