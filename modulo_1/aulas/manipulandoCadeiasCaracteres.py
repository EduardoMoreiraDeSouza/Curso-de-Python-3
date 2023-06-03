cadeiaCaracteres = 'Curso em Vídeo Python'

print(cadeiaCaracteres[0::3])

print(len(cadeiaCaracteres))

print(cadeiaCaracteres.count('o', 0, 13))

print(cadeiaCaracteres.find('deo'))

if ('Curso' in cadeiaCaracteres):
    print("True")
else:
    print("False")

novaCadeiaCaracteres = cadeiaCaracteres.replace('Python', 'Android')
novaCadeiaCaracteres = cadeiaCaracteres.upper()
novaCadeiaCaracteres = cadeiaCaracteres.lower()
novaCadeiaCaracteres = cadeiaCaracteres.capitalize()  # Primeira letra da frase em maiúscula
novaCadeiaCaracteres = cadeiaCaracteres.title()  # Cada palavra com a letra da frase em maiúscula
novaCadeiaCaracteres = cadeiaCaracteres.strip()
novaCadeiaCaracteres = cadeiaCaracteres.lstrip()
novaCadeiaCaracteres = cadeiaCaracteres.rstrip()

cadeiaCaracteresArray = cadeiaCaracteres.split()
cadeiaCaracteresJuntandoArrays = ' '.join(cadeiaCaracteresArray)
