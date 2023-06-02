""" Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa. """

from math import hypot

catetoOposto = float(input('Digite o valor do cateto Oposto do triângulo: '))
catetoAdjacente = float(input('Digite o valor do cateto Adjacente do triângulo: '))

hipotenusa = hypot(catetoOposto, catetoAdjacente)

print('O comprimento da hipotenusa é: {}'.format(hipotenusa))
