nome = input('Qual é o seu nome? ')

if nome == "Eduardo":
    print('Que nome bonito!')

elif nome == "Pedro" or nome == "Maria" or nome == "Paulo":
    print('Seu nome é bem popular no Brasil!')

elif nome in "Ana Cláudio Jéssica Juliano":
    print('Que belo nome feminino você tem!')

else:
    print('Seu nome é bem normal!')

print('Tenha um ótimo dia {}!'.format(nome))
