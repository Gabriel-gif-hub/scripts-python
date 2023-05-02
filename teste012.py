nome = str(input('Digite seu nome:'))
if nome == 'Gabriel':
    print('Você tem um nome bonito em!')
elif nome == 'Maria' or nome == 'Pedro' or nome == 'João':
    print('Nome popular no Brasil')
elif nome in 'Joana Paula Mariana Silva':
    print('Belo nome')
else:
    print('Que nome normal!')
