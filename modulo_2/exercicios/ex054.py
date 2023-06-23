"""
Criie um programa que leia o ano ed nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade  quantas já são maiores.

"""
import datetime
from datetime import date

maioridadeSim = 0
maioridadeNao = 0

for c in range(0, 7):

    anoNascimento = int(input("Por favor, digite o ano do seu nascimento: "))
    idade = date.today().year - anoNascimento

    if idade >= 18:
        maioridadeSim += 1
    else:
        maioridadeNao += 1

print("{} pessoa(s) já atingiram a maioridade, e {} pessoa(s) ainda não atingiram a maioridade!".format(maioridadeSim, maioridadeNao))
