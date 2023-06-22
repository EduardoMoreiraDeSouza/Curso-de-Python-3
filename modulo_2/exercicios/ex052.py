"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

"""

numero = int(input("Digite um número inteiro: "))

quantDivisores = 1

if numero == 1:
    print('O número {} não é um número primo!'.format(numero))

for c in range(1, numero):
    if numero % c == 0:
        quantDivisores += 1
    if quantDivisores > 2:
        print('O número {} NÃO é um número primo!'.format(numero))
        exit()

if quantDivisores == 2:
    print('O número {} É um número primo!'.format(numero))
