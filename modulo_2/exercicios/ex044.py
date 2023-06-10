"""
Elabore um programa que calcule o valor a a ser pago por um produto,
considerando o seu preço normal e a condição de pagamento:

- A vista (dinheiro ou cheque): 10% de desconto;
- A vista no cartão: 5% de desconto;
- Em até 2x no cartão: Preço normal;
- 3x ou mais no cartão: 20% de juros;

"""

precoProduto = float(input('Por favor! Dite o preço do produto: '))
formaPagamento = int(input('1: À vista no dinheiro ou cheque\n2: A vista no cartão\n3: Em até 2x no cartão\n4: 3x ou mais no cartão\nForma de Pagamento de 1 a 4: '))

while 1 > formaPagamento < 4:
    formaPagamento = int(input('1: À vista no dinheiro ou cheque\n2: A vista no cartão\n3: Em até 2x no cartão\n4: 3x ou mais no cartão\nForma de Pagamento de 1 a 4: '))

if formaPagamento == 1:
    precoProduto = precoProduto - precoProduto / 100 * 10
    print('Você ganhou 10% de desconto! O preço a se pagar é R${:.2f}'.format(precoProduto))

elif formaPagamento == 2:
    precoProduto = precoProduto - precoProduto / 100 * 5
    print('Você ganhou 5% de desconto! O preço a se pagar é R${:.2f}'.format(precoProduto))

elif formaPagamento == 3:
    print('Você parcelou em 2x! O preço a se pagar é R${:.2f} sem nenhum juros!'.format(precoProduto))

else:
    precoProduto = precoProduto + precoProduto / 100 * 20
    print('O preço a se pagar é R${:.2f} com 20% de juros!'.format(precoProduto))
