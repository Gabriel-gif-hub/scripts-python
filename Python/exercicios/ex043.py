print('======Desafio 043======')
"""
Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

- abaixo de 18.5: ABAIXO DO PESO;
- Entre 18.5 e 25: PESO IDEAL:
- 25 até 30: SOBREPESO;
- 30 até 40: OBESIDADE;
- Acima de 40: OBESIDADE MÓRBIDA.
"""
print('CÁCULO DO IMC (Ìndice de Massa Corpórea)')
peso = float(input('Digite o seu peso atual: '))
altura = float(input('Digite a sua altura atual: '))
imc = peso/altura**2
print('IMC: {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
    print('Vai comer logo meu!')
elif imc >= 18.5 and imc <= 24.99:
    print('Você está com o PESO IDEAL!')
    print('Parabéns!')
elif imc >= 25 and imc <= 29.99:
    print('Você está com SOBREPESO!')
    print('Umas corridinhas matinas resolveram isso!')
elif imc >=30 and imc <= 40:
    print('Você está com OBESIDADE!')
    print('Procure um nutricionista e vá para a academia!')
elif imc > 40:
    print('Você está com OBESIDADE MÓRBIDA!')
    print('PROCURE UM MÉDICO IMEDIATAMENTE!')
