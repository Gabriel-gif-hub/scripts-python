print('======Desafio 077======')
"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
listagem = ('Aprender','Ensinar','Python','Porgramacao','Codigo','Estagio','Repeticao','Condicao','Constancia')

for c in listagem:
    print(f'\nNa palavra {c.upper()} temos as vogais: ',end='')
    for l in c:
        if l.lower() in 'aeiou':
            print(l.lower(),end='')
