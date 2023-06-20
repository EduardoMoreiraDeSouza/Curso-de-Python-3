"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.

"""

soma = 0

for c in range(1, 7):
    numero = int(input('{}º número inteiro: '.format(c)))
    if numero % 2 == 0:
        soma += numero

print('\nA soma de todos os números pares escolhidos, é: {}'.format(soma))
