from math import hypot

catetoOposto = float(input('Digite o valor do cateto Oposto do triângulo: '))
catetoAdjacente = float(input('Digite o valor do cateto Adjacente do triângulo: '))

hipotenusa = hypot(catetoOposto, catetoAdjacente)

print('O comprimento da hipotenusa é: {}'.format(hipotenusa))

