""" Faça um programa que leia um número inteiro qualquer, e mostre na tela a sua tabuada. """

numero = int(input('Digite um valor: '))
contador = 0

while contador <= 9:
    multiplicacao = numero * contador
    print('{} X {}: {}'.format(numero, contador, multiplicacao))
    contador += 1
