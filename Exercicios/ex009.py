numero = int(input('Digite um valor: '))
contador = 0

while (contador <= 9) :
    multiplicacao = numero * contador
    print('{} X {}: {}'.format(numero, contador, multiplicacao))
    contador += 1