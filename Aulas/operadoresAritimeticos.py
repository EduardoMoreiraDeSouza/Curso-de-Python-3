n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
potencia = n1 ** n2
divisaoInteira = n1 // n2
restoDaDivisao = n1 % n2

print('A Soma de {} e {} é: {}'.format(n1, n2, soma))
print('A Subtração de {} e {} é: {}'.format(n1, n2, subtracao))
print('A Multiplicação de {} e {} é: {}'.format(n1, n2, multiplicacao))
print('A Divisão de {} e {} é: {}'.format(n1, n2, divisao))
print('A Potência de {} e {} é: {}'.format(n1, n2, potencia))
print('A divisão inteira de {} e {} é: {}'.format(n1, n2, divisaoInteira))
print('O resto da divisão de {} e {} é: {}'.format(n1, n2, restoDaDivisao))