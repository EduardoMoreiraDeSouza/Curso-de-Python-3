dolar = 4.956
print('Valor do Dólar: {}\n'.format(dolar))

valor = float(input('Digite quantos reais você quer trocar em dólares: '))

cambio = valor / dolar

print('Com {} valor em reais, é possível comprar {} dólares!'.format(valor, cambio))