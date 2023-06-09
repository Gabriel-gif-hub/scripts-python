print('======Desafio 083======')
"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

expr = str(input('Digite uma expressão: '))

listagem = []

for simb in expr:
    if simb == ('('):
        listagem.append('(')
    elif simb == (')'):
        if len(listagem) > 0:
            listagem.pop()
        else:
            listagem.append(')')
            break

if len(listagem) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida!')
