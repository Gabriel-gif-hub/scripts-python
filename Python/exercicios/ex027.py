print('======Desafio 027======')
"""
Faça um programa que leia o nome completo de um a pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
"""
nome = str(input('Digite o seu nome completo: ')).strip()
n = nome.split()
print('Seu nome completo é {}, correto?'.format(nome.title()))
print('Seu primeiro nome é {}'.format(n[0]).title())
print('Seu último nome é {}'.format(n[len(n)-1].title()))

