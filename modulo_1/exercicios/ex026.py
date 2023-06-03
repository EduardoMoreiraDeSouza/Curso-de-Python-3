"""
Faça um programa que leia uma frase pelo teclado e mostre
    Quantas vezes aparece a letra 'a';
    Em que posição ela aparece a primeira vez;
    emq eu posição ela aparece a ultima vez;
"""

frase = input("Digite uma frase: ").lower()

quantidadeLetraA = frase.count("a")
primeiraLetraA = frase.find("a")
ultimaLetraA = frase.rfind("a")

print("A frase que você digitou, tem {} letras 'a', sua primeira aparição da letra 'a' é na posição {} e sua ultima "
      "aparição é na posição {}.".format(quantidadeLetraA, primeiraLetraA, ultimaLetraA))
