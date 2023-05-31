from math import cos
from math import tan
from math import sin
from math import radians

angulo = radians(float(input('Digite um ângulo qualquer: ')))

cosseno = cos(angulo)
tangente = tan(angulo)
seno = sin(angulo)

print('Seno: {:.5f}\nCosseno: {:.5f}\nTangente: {:.5f}'.format(seno, cosseno, tangente))