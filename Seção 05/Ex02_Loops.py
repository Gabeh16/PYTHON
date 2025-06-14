"""
Faça um programa que utilize o comando while para
mostrar na tela uma contagem regressiva, iniciando em
10 e terminando em 0. Mostre também uma mensagem "FIM"
após a contagem.
"""

contador: int = 10

while contador >= 0:
    print(contador)
    contador = contador - 1
print('FIM')