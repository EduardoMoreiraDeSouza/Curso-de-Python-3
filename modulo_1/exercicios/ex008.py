""" Escreva um programa que leia um valor em metros e o exiba convertido em centímentros e milímetros. """

metros = float(input('Digite um valor em metros: '))

centimentros = metros * 100
milimetros = metros * 1000

print('{}m em centímentros é: {}'.format(metros, centimentros))
print('{}m em milímetros é: {}'.format(metros, milimetros))
