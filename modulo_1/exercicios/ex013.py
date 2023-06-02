""" Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento. """

salario = float(input('Digite o valor do seu salário: '))

novoSalario = salario + ((salario / 100) * 15)

print('Seu novo salário com 15% de aumento é: {}'.format(novoSalario))
