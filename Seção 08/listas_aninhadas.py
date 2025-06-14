"""
Listas aninhadas

- Algumas linguagens de programação (C/Java) possuem uma estrutura de dados chamados de arrays
    - Unidimensionais (Arrays/Vetores):
    - Multidimencionais (Matrizes):

Em pyrhon nós temos as Listas

numeros = [1,'b',3.22,True,5]

# Exemplos

listas = [[1,2,3],[4,5,6],[7,8,9]]

print(listas)

# Como faço para acessar os dados?

print(listas[0][1]) # 2

print(listas[2][1]) # 8

# Exemplos

listas = [[1,2,3],[4,5,6],[7,8,9]] # Matriz 3*3

# Iterando com loops em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num)

# List Comprehension

[print(valor) for valor in lista for lista in listas]

"""

# Outros exemplos

# Gerando um tabuleiro 3x3
tabuleiro = [[numero for numero in range(1,4)]for valor in range(1,4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1,4) ] for valor in range(1,4)]

# Gerando valores iniciais

print([['*' for i in range(1,4)]for j in range(1,4)])
