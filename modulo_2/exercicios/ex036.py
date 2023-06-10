"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa
vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar o empréstimo.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado.

"""

valorCasa = float(input('Qual o valor da casa que você pretende comprar? '))
salario = float(input('Qual o valor do seu salário mensal? '))
prazo = int(input('Em quantos anos você pretende pagar o empréstimo? '))

prestacaoMensal = valorCasa / (prazo * 12)
valorMaximoPrestacao = (salario / 100) * 30

if prestacaoMensal > valorMaximoPrestacao:
    print('Empréstimo Negado!')

else:
    print('Parabéns! Seu empréstimo foi aprovado!\nSuas prestações serão de R${:.2f} por prazo anos.'.format(prestacaoMensal))
