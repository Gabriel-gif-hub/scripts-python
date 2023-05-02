print('======Desafio 012======')
# Faça um algoritmo que leia o preço de um produtoe mostre seu novo preço, com 5% de desconto
preco = float(input('Digite o valor do  produto para obter seu desconto: '))
resto = (preco*0.05)
desconto = (preco-resto)
print('Com o desconto (5% = R%{:.2f}) aplicado sobre os R${:.2f} seu novo valor é de R${:.2f} '.format(resto,preco,desconto))
