"""
Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher,
só que agora faça utilizando um laço for.

"""

numero = int(input('Digite um valor: '))

for c in range(0, 11):
    multiplicacao = numero * c
    print('{} X {}: {}'.format(numero, c, multiplicacao))
