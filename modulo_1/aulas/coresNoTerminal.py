""" Style 0: none, 1: bold, 4: underline, 7: negative
    Cores: 30: branco, 31: vermelho, 32: verde, 33: amarelo, 34: azul, 35: majenta, 36: ciano, 37:cinza.
    Back: 40: branco, 41: vermelho, 42: verde, 43: amarelo, 44: azul, 45: majenta, 46: ciano, 47:cinza.

\033[style text back m """

cores = {
    'limpa': '\033[m',
    'azulSublinhado': '\033[4:34m'
}

print("{}Olá, Mundo!{}".format(cores['azulSublinhado'], cores['limpa']))
