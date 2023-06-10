"""
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o ultimo nome separadamente.

"""

nomeCompleto = input("Por favor! Digite seu nome completo: ").title()

nomeArray = nomeCompleto.strip().split()
primeiroNome = nomeArray[0]
ultimoNome = nomeArray[len(nomeArray)-1]

print("Seu primeiro nome é '{}' e o seu último nome é '{}'".format(primeiroNome, ultimoNome))
