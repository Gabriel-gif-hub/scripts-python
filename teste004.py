n1 = float(input('Digite um número:'))
n2 = float(input('Digite outro número:'))
s = n1+n2
sub = n1-n2
d = n1/n2
di = n1//n2
r = n1%n2
e = n1**n2
print('A soma vale: {}, a subtração vale: {}, a divisãp vale: {:.2f}'.format(s,sub,d))
print('A divisão inteira vale: {}, o resto vele: {}, a exponensiação vale: {:.2f}'.format(di,r,e))
# Os sinas (:.númerof) dentro das chaves são formas de pedir para o programa apresentar somente dois número após a vírgula
# Para não quebrar a linha de um print para o outro, basta add o comando (end='') antes do último parenteses
# Para quebrar a linha de um print basta add aonde desejar a quebra com \n

