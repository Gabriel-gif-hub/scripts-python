valores = []

while True:
    valores.append(int(input('Digite um valor:')))
    while True:
        opcao = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
        if opcao in 'NS':
            break
    if opcao == 'N':
        break

for c,v in enumerate(valores):
    print(f'Os valores são: {v} e a posição: {c}')
print('Fim')

