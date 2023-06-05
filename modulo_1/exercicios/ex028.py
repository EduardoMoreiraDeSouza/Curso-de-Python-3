"""
    Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

    O programa deverá escrever na tela se o se o usário venceu ou perdeu.
 """

from random import randint
from time import sleep

numeroAleatorio = randint(0, 5)
numeroUsuario = int(input("Pensei em um número de 0 a 5! Que número é esse!? "))

print("Processando...")
sleep(3)

if numeroUsuario == numeroAleatorio:
    print("Parabéns! você acertou!!")

else:
    print("Ops! Você perdeu! O número que eu pensei foi {}".format(numeroAleatorio))