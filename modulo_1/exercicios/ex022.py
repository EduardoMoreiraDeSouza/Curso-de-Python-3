"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
    O nome com todas as letras maiúsculas;
    O nome com todas as letras minúsculas;
    Quantas letras ao todo (Sem considerar espaços);
    Quantas letras tem o primeiro nome;
"""

nomeCompleto = input("Por favor! Digite seu nome completo: ")

letrasMaiusculas = nomeCompleto.upper()
letrasMinusculas = nomeCompleto.lower()
quantLetras = len(nomeCompleto.replace(" ", ""))
quantLetrasPrimeiroNome = len(nomeCompleto.split()[0])

print("\nOlá {}\n".format(nomeCompleto.split()[0]))

print("Seu nome em letras maiúsculas: {}\n".format(letrasMaiusculas))
print("Seu nome em letras minúsculas: {}\n".format(letrasMinusculas))
print("Seu nome tem {} caracteres! (Sem espaços)\n".format(quantLetras))
print("Seu primeiro nome tem {} caracteres!".format(quantLetrasPrimeiroNome))
