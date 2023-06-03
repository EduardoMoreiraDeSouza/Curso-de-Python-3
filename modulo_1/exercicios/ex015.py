""" Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado, e a quantidade de dias
pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,
15 por Km rodado."""

diasAlugado = int(input('Por quantos dias o carro ficou alugado? '))
kmRodados = float(input('Quantos quilômetros o carro percorreu durante o aluguel? '))

valorDias = diasAlugado * 60
valorKm = kmRodados * 0.15
precoFinal = valorDias + valorKm

print('O total a pagar é R${:.2f}, sendo R${:.2f} pelos dias alugados e R${:.2f} pelos quilômetros rodados'.format(precoFinal, valorDias, valorKm))
