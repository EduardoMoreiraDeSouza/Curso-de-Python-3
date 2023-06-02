""" Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. """

preco = float(input('Digite o valor do produto: '))

novoPreco = preco - ((preco / 100) * 5)

print('O valor do produto com 5% de desconto é: {}'.format(novoPreco))
