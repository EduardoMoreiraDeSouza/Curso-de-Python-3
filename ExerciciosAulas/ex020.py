from random import shuffle

nome1 = input('Digite o nome do primeiro aluno: ')
nome2 = input('Digite o nome do segundo aluno: ')
nome3 = input('Digite o nome do terceiro aluno: ')
nome4 = input('Digite o nome do quarto aluno: ')

ordemApresentacao = [nome1, nome2, nome3, nome4]
shuffle(ordemApresentacao)

print('A ordem de apresentação será\n{}'.format(ordemApresentacao))