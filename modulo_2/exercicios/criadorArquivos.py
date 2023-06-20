ultimoExercicioFeito = 55 + 1
ultimoExercicio = 56


while ultimoExercicioFeito <= ultimoExercicio:
    nome = 'ex0' + str(ultimoExercicioFeito) + '.py'
    open(nome, 'w')
    ultimoExercicioFeito += 1
