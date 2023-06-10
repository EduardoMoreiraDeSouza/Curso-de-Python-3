"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida.

- Média abaixo de 5.0: REPROVADO;
- Média entre 5.0 e 6.9: RECUPERAÇÃO;
- Média 7.0 ou superior: APROVADO;

"""

nota1 = float(input('Digite a nota da sua primeira prova: '))
nota2 = float(input('Digite a nota da sua segunda prova: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Sua média foi de {:.1f} ponto(s)! Você foi reprovado!'.format(media))

elif 5 <= media <= 6.9:
    print('Sua média foi de {:.1f} ponto(s)! Você está de recuperação!'.format(media))

else:
    print('Sua média foi de {:.1f} ponto(s)! Você foi Aprovado! PARABÉNS!!'.format(media))
