"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alista ao servço militar;
- Se é a hora de se alistar;
- Se já passou do tempo do alistamento;

Seu programa também deverá mostrar o campo que falta ou que passou do prazo.

"""

from datetime import date

anoNascimento = int(input('Digite o ano que você nasceu: '))
anoAtual = date.today().year

idade = anoAtual - anoNascimento

if idade < 18:
    print('Você ainda irá se alistar no exército! Falta {} ano(s)!'.format(18 - idade))

elif idade == 18:
    print('Está na hora de você se alistar no exército!')

else:
    print('Você já passou do prazo de se alistar no exército! Já se passaram {} ano(s)!'.format(idade - 18))

