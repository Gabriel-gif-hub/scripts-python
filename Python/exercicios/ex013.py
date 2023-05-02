print('======Desafio 013======')
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo 
# salário com um aumento de 15%
salario = float(input('Digite o valor do seu salário: '))
aumento = (salario*0.15)
total = (salario+aumento)
print('Com o último aumento nos salários (15%), seu novo salário é de R${:.2f}'.format(total))
