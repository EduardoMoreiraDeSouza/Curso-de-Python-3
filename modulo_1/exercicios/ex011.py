""" Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta nescessária para pintá-la, sabendo que cada litro de tinta, pinta uma área ed 2m² """

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura * largura
quantidadeTinta = area / 2

print('Sua parede tem uma área de {}m² e será nescessário {} litros de tinta para pinta-la'.format(area, quantidadeTinta))
