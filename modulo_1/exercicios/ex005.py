""" FAça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor. """

numero = int(input('Digite um valor: '))

antecessor = numero - 1
sucessor = numero + 1

print('O antecessor do número {0} é {1}, e o sucessor do número {2} é {3}!'.format(numero, antecessor, numero, sucessor))
