a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
soma = a + b
print(' A soma dos valores \033[34m{}\033[m e \033[34m{}\033[m é \033[1;30;46m{}\033[m'.format(a,b,soma))

# A sintaxe de execução de cores no terminal python é ' \003[STYLE;TEXT;BACKm '

# Se desejar que não seja aplicado em tudo, só fechar com a mesma sintaxe.

