""" Desenvova um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas. """

distancia = float(input("Digite a distância em Km da sua viagem: "))

if distancia <= 200:
    preco = distancia * 0.5
    print("O custo total da sua viagem será R${:.2f}".format(preco))

else:
    preco = distancia * 0.45
    print("O custo total da sua viagem será R${:.2f}".format(preco))
