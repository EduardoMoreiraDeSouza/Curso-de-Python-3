altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura * largura
quantidadeTinta = area / 2

print('Sua parede tem uma área de {}m² e será nescessário {} litros de tinta para pinta-la'.format(area, quantidadeTinta))
