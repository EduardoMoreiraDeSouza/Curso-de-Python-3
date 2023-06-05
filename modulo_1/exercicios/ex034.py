""" Escreva um programa que pergunte o salário de um fuuncionário e calcule o valor do seu aumento.
        Para salários superiores a R$1200,00, calcule um aumento de 10% e para inferiores a isso, 10% """

salario = float(input("Por favor! Digite o seu salário: "))

if salario > 1250:
    salario += salario / 100 * 10

else:
    salario += salario / 100 * 15

print("Seu novo salário será R${:.2f}".format(salario))
