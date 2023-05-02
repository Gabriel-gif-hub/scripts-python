print('======Desafio 044======')
"""
Elabore um programa que calcule o valor do produto considerando o seu preço normal e condição de pagamentos:

- Á vista no dinheiro/cheque ou pix: 10% de desconto
- Á vista no cartão: 5% de desconto
- Em até 2 vezes no cartão: preço normal
- 3 vezes ou mais no cartão: 20% de juros
"""

print('======LOJAS OLIVEIRA======')
valor = float(input('Digite o valor do produto: '))
print('------CONDIÇÕES DE PAGAMENTO------')
print('Digite uma das opções abaixo:')
print('[ 1 ] à vista no dinheiro/cheque ou pix')
print('[ 2 ] à vista no cartão')
print('[ 3 ] em até 2 vezes no cartão')
print('[ 4 ] 3 vezes ou mais no cartão')
opcao = int(input('Digite uma das opções acima: '))
if opcao == 1:
    desconto = valor-(valor*0.1)
    print(
        'Sua compra de R${:.2f} à vista no dinheiro/cheque ou pix sairá por:'.format(valor))
    print('R${:.2f}'.format(desconto))
elif opcao == 2:
    desconto = valor-(valor*0.05)
    print('Sua compra de R${:.2f} à vista no cartão sairá por:'.format(valor))
    print('R${:.2f}'.format(desconto))
elif opcao == 3:
    p1 = valor/2
    print(
        'Sua compra parcelada em 2 vezes sairá no preço normal de R${:.2f}'.format(valor))
    print('Em R${:.2f} por 2 meses'.format(p1))
elif opcao == 4:
    juros = valor+(valor*0.2)
    parcelas = int(input('Digite a quantidade de parcelas:'))
    p1 = juros/parcelas
    if parcelas <= 12:
        print('Sua compra parcelada em {} vezes sairá por: R${:.2f} (com juros)'.format(parcelas,juros))
        print('Em R${:.2f} por {} meses'.format(p1,parcelas))

    else:
        print('Parcelamos em até 12 vezes!')
else:
    print('Opção inválida')
