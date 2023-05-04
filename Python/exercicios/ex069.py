print('======Desafio 069======')
"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
"""

mais_18 = masculino = f_menor_20 = 0

while True:
    print('='*30)
    idade = int(input('Digite a Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Digite o Sexo: ')).upper().strip()[0]
    if idade >= 18:
        mais_18 += 1
    if sexo == 'M':
        masculino += 1
    if sexo == 'F' and idade < 20:
        f_menor_20 += 1
    
    continuar = ' '
    print('='*30)
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if continuar == 'N':
        break

print('='*30)
print(f"""Pessoas maiores de 18: {mais_18}
Homens cadastrados: {masculino}
Mulheres menores de 20 anos: {f_menor_20}""")
