""" Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem
dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite """

velocidade = float(input("Digite a velocidade atual: "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Você ultrapassou a velocidade máxima de 80km/h!! E foi multado em R${:.2f}".format(multa))

else:
    print("Você está dentro do limite de velocidade! Pode seguir viagem!")
