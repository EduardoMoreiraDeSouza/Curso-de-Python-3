"""
A Confederação Nacional de Natação, precisa de um programa que leia o ano de nascimento de um atlera e mostre
sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM;
- Até 14 anos: INFANTIL;
- Até 19 anos: JÚNIOR;
- Até 20 anos: SÊNIOR;
- Acima: MASTER;

"""

from datetime import date

anoNascimento = int(input('Olá Atleta!! Por favor! Digite o ano do seu nascimento: '))
anoAtual = date.today().year

idade = anoAtual - anoNascimento

if idade <= 9:
    print('Você é um atleta MIRIM!')

elif idade <= 14:
    print('Você é um atleta INFANTIL!')

elif idade <= 19:
    print('Você é um atleta JÚNIOR!')

elif idade <= 20:
    print('Você é um atleta SÊNIOR!')

else:
    print('Você é um atleta MASTER!')
