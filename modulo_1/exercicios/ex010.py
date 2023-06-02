""" Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e mostre quantos dólares ela pode comprar. """

dolar = 4.956
print('Valor do Dólar: {}\n'.format(dolar))

valor = float(input('Digite quantos reais você quer trocar em dólares: '))

cambio = valor / dolar

print('Com {} valor em reais, é possível comprar {} dólares!'.format(valor, cambio))
