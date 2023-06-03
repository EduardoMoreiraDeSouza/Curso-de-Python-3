""" Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo' """

cidade = input("Digite o nome de uma cidade qualquer: ").lower()

if cidade.find('santo') != 0:
    print("Essa cidade NÃO COMEÇA com a palavra Santo")

else:
    print("Essa cidade COMEÇA com a palavra Santo")
