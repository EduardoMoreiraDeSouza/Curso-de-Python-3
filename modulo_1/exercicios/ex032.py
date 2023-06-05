""" Faça um programa que leia um nome qualquer e mostre se ele é bissexto """

ano = int(input("Digite um ano qualquer, ou zero para analizar o ano atual: "))

from datetime import date

if ano == 0:
    ano = date.today().year

resto4 = ano % 4
resto100 = ano % 100
resto400 = ano % 400

if resto4 == 0:
    if resto100 != 0:
        print("O ano de {} é bissexto!".format(ano))
    else:
        print("O ano de {} não bissexto!".format(ano))

else:
    if resto400 == 0:
        print("O ano de {} é bissexto!".format(ano))
    else:
        print("O ano de {} não bissexto!".format(ano))