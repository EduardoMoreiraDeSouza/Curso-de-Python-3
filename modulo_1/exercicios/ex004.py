""" Faça um programa que leia algo pelo teclado,
e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele. """

dado = input('Digite qualquer coisa que você desejar: ')

numero = dado.isnumeric()
letras = dado.isalpha()
somenteLetrasMaiusculas = dado.isupper()
somenteLetrasMinusculas = dado.islower()

print('{} é um número? {}'.format(dado, numero))
print('{} contém somente letras? {}'.format(dado, letras))
print('{} contém somente caracteres maiúsculos? {}'.format(dado, somenteLetrasMaiusculas))
print('{} contém somente caracteres minúsculos? {}'.format(dado, somenteLetrasMinusculas))
