"""
Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão.

"""

numero = int(input('Digite um número inteiro qualquer: '))
numeroEscolhido = numero

baseConversao = int(input('\n1 para Binário\n2 para Octal\n3 para Hexadecimanl\nEscolha a base de conversão: '))

while baseConversao < 1 or baseConversao > 3:

    baseConversao = int(input('\n1 para Binário\n2 para Octal\n3 para Hexadecimanl\nEscolha uma base de conversão aceita: '))

todosRestosDivisoes = []

if baseConversao == 1:

    baseConversao = "Binário"

    while numero > 0:

        todosRestosDivisoes.insert(0, numero % 2)
        numero = numero // 2

if baseConversao == 2:

    baseConversao = "Octal"

    while numero > 0:

        todosRestosDivisoes.insert(0, numero % 8)
        numero = numero // 8

if baseConversao == 3:

    baseConversao = "Hexadecimal"

    while numero > 0:

        restoDivisao = numero % 16

        if restoDivisao > 9:
            if restoDivisao == 10:
                restoDivisao = "A"

            elif restoDivisao == 11:
                restoDivisao = "B"

            elif restoDivisao == 12:
                restoDivisao = "C"

            elif restoDivisao == 13:
                restoDivisao = "D"

            elif restoDivisao == 14:
                restoDivisao = "E"

            elif restoDivisao == 15:
                restoDivisao = "F"

        todosRestosDivisoes.insert(0, restoDivisao)
        numero = numero // 16


resultadoConversao = ''
for i in range(len(todosRestosDivisoes)):
    resultadoConversao = resultadoConversao + str(todosRestosDivisoes[i])

print('O número {} convertido na base {} é {}'.format(numeroEscolhido, baseConversao, resultadoConversao))
