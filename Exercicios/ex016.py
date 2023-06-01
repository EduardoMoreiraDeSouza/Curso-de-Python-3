from math import trunc

numeroReal = float(input('Digite um número real: '))

parteInteira = trunc(numeroReal)

print('Parte inteira do número {} é {}'.format(numeroReal, parteInteira))