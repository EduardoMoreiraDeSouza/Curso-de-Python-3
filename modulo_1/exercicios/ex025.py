""" Crie um programa que leia o nome de uma pessoa ee diga se ela tem 'Silva no nome' """

nome = input("Por favor! Digite o nome de uma pessoa: ").lower()

if nome.find('silva') != -1:
    print('Esse nome CONTÉM Silva!')
else:
    print('Esse nome NÃO CONTÉM Silva!')
