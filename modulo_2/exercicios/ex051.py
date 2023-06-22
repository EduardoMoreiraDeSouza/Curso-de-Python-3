"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiro termos dessa progressão.

"""

termo = int(input("Primeiro termo de uma PA: "))
razao = int(input("Razão da PA: "))

for c in range(0, 10):
    print('{} -->'.format(termo), end=' ')
    termo += razao

print('Fim')
