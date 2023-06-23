"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido.

"""

lista = []

for c in range(0, 5):
    peso = float(input("Por favor informe seu peso: "))
    lista.append(peso)

lista = sorted(lista)

print("O maior valor é {} e o menor é {}".format(lista[4], lista[0]))
