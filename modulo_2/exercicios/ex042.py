"""
Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado;

- Equilátero: Todos os lados iguais;
- Isósceles: Dois lados iguais;
- Escaleno: Todos os lados diferentes;

"""

""" Desenvolver um programa que leia o comprimento de três retas e diga ao usuário
 se elas podem ou não formar um triângulo. """

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

    if retaA == retaB:
        if retaB == retaC:
            tipoTriangulo = "equilátero"
        else:
            tipoTriangulo = "isóceles"

    elif retaA == retaC:
        if retaB == retaC:
            tipoTriangulo = "equilátero"
        else:
            tipoTriangulo = "isóceles"

    elif retaB == retaC:
        if retaB == retaA:
            tipoTriangulo = "equilátero"
        else:
            tipoTriangulo = "isóceles"

    else:
        tipoTriangulo = "escaleno"

    print("É possível formar um triângulo {} com essas três retas!".format(tipoTriangulo))
else:
    print("Não é possível formar um triângulo com essas três retas!")

