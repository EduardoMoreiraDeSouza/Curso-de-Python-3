"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso ideal;
- Entre 18.5 e 25: Peso ideal;
- 25 até 30: Sobrepeso;
- 30 até 40: Obesidade;
- Acima de 40

"""

peso = float(input('Olá! Por favor! Digite seu peso: '))
altura = float(input('Ótimo! Agora, digite sua altura: '))

imc = peso / altura ** 2

if imc < 18.5:
    print('ATENÇÃO!! Você está abaixo do peso ideal!')

elif imc <= 25:
    print('PARABÉNS!! Você está no seu peso ideal!')

elif imc <= 30:
    print('ATENÇÃO!! Você está um pouco acima do seu peso ideal! (Sobrepeso)')

elif imc <= 40:
    print('ATENÇÃO!! Você está muito acima do seu peso ideal! (Obesidade)')

else:
    print('ATENÇÃO!! Você está extremamente acima do seu peso ideal! (Obesidade Mórbida)')
