print('======Desafio 053======')
"""
Crie um programa que leia um frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
"""
print('=== LEITOR DE PALÍNDROMO ===')
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for c in range(len(junto) -1,-1,-1):
    inverso += junto[c]
print('FRASE: {} \nINVERSO: {}'.format(junto,inverso))
if junto == inverso:
    print('TEMOS UM PALÍNDROMO!')
else:
    print('NÃO TEMOS UM PALÍNDROMO!')
