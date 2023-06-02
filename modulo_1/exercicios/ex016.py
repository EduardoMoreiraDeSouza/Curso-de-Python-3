""" Crie um programa que leia um número real qualquer pelo teclado, e mostre na tela a sua porção inteira. """

from math import trunc

numeroReal = float(input('Digite um número real: '))

parteInteira = trunc(numeroReal)

print('Parte inteira do número {} é {}'.format(numeroReal, parteInteira))
