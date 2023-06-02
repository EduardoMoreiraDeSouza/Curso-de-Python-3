import math

numero = float(input('Digite um valor: '))

raiz = math.sqrt(numero)
arrendondarCima = math.ceil(numero)
arrendondarBaixo = math.floor(numero)

print('Raiz {} \n Arredondamento para cima {} \n Arredondamento para baixo {}'.format(raiz, arrendondarCima, arrendondarBaixo))
