""" Crie um programa que faça o computador jogar jokenpô com você. """

from random import randint

jogador = int(input('1: PEDRA\n2: PAPEL\n3: TESOURA\nO que você escolhe de 1 a 3? '))

while 1 > jogador < 3:
    jogador = int(input('1: PEDRA\n2: PAPEL\n3: TESOURA\nO que você escolhe de 1 a 3? '))


computador = randint(1, 3)

if computador == 1:
    escolhaComputador = 'pedra'

elif computador == 2:
    escolhaComputador = 'papel'

elif computador == 3:
    escolhaComputador = 'tesoura'


if computador == jogador:
    print("Eu escolhi {}! Empatamos!".format(escolhaComputador))


elif computador == 1 and jogador == 2:
    print("Você ganhou! PARABÉNS! Eu escolhi {}!".format(escolhaComputador))

elif computador == 2 and jogador == 3:
    print("Você ganhou! PARABÉNS! Eu escolhi {}!".format(escolhaComputador))

elif computador == 3 and jogador == 1:
    print("Você ganhou! PARABÉNS! Eu escolhi {}!".format(escolhaComputador))


elif jogador == 1 and computador == 2:
    print("Eu ganhei! Pois eu escolhi {}!".format(escolhaComputador))

elif jogador == 2 and computador == 3:
    print("Eu ganhei! Pois eu escolhi {}!".format(escolhaComputador))

elif jogador == 3 and computador == 1:
    print("Eu ganhei! Pois eu escolhi {}!".format(escolhaComputador))
