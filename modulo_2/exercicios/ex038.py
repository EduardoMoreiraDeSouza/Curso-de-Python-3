"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior;
- O segundo valor é maior;
- Não existe valor maior, os dois são iguais;

"""

numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))

if numero1 > numero2:
    print('O primeiro valor é maior que o segundo {} > {}'.format(numero1, numero2))

elif numero1 < numero2:
    print('O segundo valor é maior que o primeiro {} > {}'.format(numero2, numero1))

else:
    print('Não existe valor maior, os dois são iguais {} = {}'.format(numero1, numero2))