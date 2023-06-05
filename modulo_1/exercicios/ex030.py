""" Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar. """

numero = int(input("Digite um número inteiro: "))

restoDivisao = numero % 2

if restoDivisao == 0:
    print("Esse número é par!")

else:
    print("Esse número é ímpar!")
