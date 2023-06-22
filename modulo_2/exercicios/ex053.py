"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

"""

frase = str(input("Digite uma frase: "))
fraseSemEspaco = frase.replace(' ', '').lower()

quantCaracteres = len(fraseSemEspaco)
acertos = 0

for c in range(0, quantCaracteres):
    if fraseSemEspaco[c] == fraseSemEspaco[(quantCaracteres - 1) - c]:
        acertos += 1

if acertos == quantCaracteres:
    print("A frase '{}' é um palíndromo!".format(frase))

else:
    print("A frase '{}' NÃO é um palíndromo!".format(frase))
