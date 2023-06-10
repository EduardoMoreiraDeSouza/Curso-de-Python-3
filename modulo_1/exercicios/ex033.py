""" Faça um programa que leia três números e mostre qual é o maior e qual é o menor. """

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
numero3 = float(input("Digite um último número: "))

if numero2 > numero1 and numero2 > numero3:
    maior = numero2

    if numero1 > numero3:
        menor = numero3

    else:
        menor = numero1

if numero1 > numero2 and numero1 > numero3:
    maior = numero1

    if numero2 > numero3:
        menor = numero3

    else:
        menor = numero2

if numero3 > numero1 and numero3 > numero2:
    maior = numero3

    if numero2 > numero1:
        menor = numero1

    else:
        menor = numero2

print("O número {} é o maior e o {} é o menor".format(maior, menor))
