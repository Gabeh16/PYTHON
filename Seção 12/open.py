"""
Uso a tag open para abrir e ler arquivos

-> open()

função para ler

-> read()

função para fechar

-> close()

Passo a passo

1- Abrir

2 - Trabalhar

3 - Fechar
"""
from os.path import split

arquivo = open("texto.text")
# Utilizo a tag READ() para ler o arquivo

print(arquivo.closed)

print(arquivo.read())

print(arquivo.closed)

arquivo.close()

print(arquivo.closed)
