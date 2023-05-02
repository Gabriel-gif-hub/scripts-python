print('======Desafio 057======')
"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" e "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
sexo = str(input('Digite o seu sexo [M/F]: ')).strip()[0].upper()
while sexo not in 'MF':
    sexo = str(input('SEXO INVÁLIDO!\n\nDigite seu sexo novamente: ')).strip()[0].upper()
print('\nSexo [ {} ] validado com sucesso!'.format(sexo)
)
