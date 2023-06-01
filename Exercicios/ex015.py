diasAlugado = int(input('Por quantos dias o carro ficou alugado? '))
kmRodados = float(input('Quantos quilômetros o carro percorreu durante o aluguel? '))

valorDias = diasAlugado * 60
valorKm = kmRodados * 0.15
precoFinal = valorDias + valorKm

print('O total a pagar é R${:.2f}, sendo R${:.2f} pelos dias alugados e R${:.2f} pelos quilômetros rodados'.format(precoFinal, valorDias, valorKm))