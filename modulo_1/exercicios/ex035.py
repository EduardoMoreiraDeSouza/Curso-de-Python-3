"""
Desenvolver um programa que leia o comprimento de três retas e diga ao usuário
 se elas podem ou não formar um triângulo.

 """

retaA = float(input("Digite o valor da reta A: "))
retaB = float(input("Digite o valor da reta B: "))
retaC = float(input("Digite o valor da reta C: "))

formaTriangulo = False

if (retaB - retaC) < retaA < retaB + retaC:
    formaTriangulo = True

    if (retaA - retaC) < retaB < retaA + retaC:
        formaTriangulo = True

        if (retaA - retaB) < retaC < retaA + retaB:
            formaTriangulo = True

        else:
            formaTriangulo = False

    else:
        formaTriangulo = False

else:
    formaTriangulo = False

if formaTriangulo:
    print("É possível formar um triângulo com essas três retas!")
else:
    print("Não é possível formar um triângulo com essas três retas!")
