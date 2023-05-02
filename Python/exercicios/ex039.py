from datetime import date
print('======Desafio 039======')
"""
Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade.

- Se ele ainda vai se alistar ao serviço militar;
- Se  é a hora de se alistar;
- Se já passou o tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou o prazo que passou.
"""
print('DIGITE O SEU SEXO:')
print('[ F ] para FEMININO')
print('[ M ] para MASCULINO')
sexo = str(input('Sexo: '))
if sexo ==  'M':
    ano = int(input('Digite seu ano de nascimento: '))
    ano_atual = date.today().year
    idade = int(ano_atual) - ano
    print('Quem nasceu em {} tem {} anos em {}'.format(ano,idade,ano_atual))
    if idade < 18:
        data = ano + 18
        tempo_restante = 18 - idade
        print('Você ainda não está no tempo de se alistar')
        if tempo_restante > 1:
            print('Ainda faltam {} anos para seu alistamento'.format(tempo_restante))
        else:
            print('Falta {} ano para seu alistamento'.format(tempo_restante))
        print('Seu alistamento será em {}'.format(ano + 18))
    elif idade == 18:
        print('Chegou a hora de você se alistar!')
        print('Se apresente o quanto antes ao posto militar!')
    elif idade > 18:
        tempo_a_mais = idade - 18
        print('Um pouco atrasado não acha?')
        print('Seu alistamente deveria ter ocorrido em {}'.format(
            ano_atual - tempo_a_mais))
else:
    print('Gênero não faz parte do grupo obrigatório para o alistamento!')
