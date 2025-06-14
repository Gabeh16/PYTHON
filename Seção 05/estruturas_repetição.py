"""
Loop FOR

loop-> Estrutura de repetição
For -> Uma dessas estruturas

Tabela de emojis Unicode
"""
#Original = U+1F600
#Modifificado = U0001f600

for num in range(1,11):
    print('\U0001F600'* num)
nome = "Gabriel Costa Diares"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)


# Exemplo 1 de for:
for letra in nome:
    print(letra, end="\n")


#Exemplo 2 de for:
for numero in lista:
    print(numero, end="")

#Exemplo 3 de for:
"""
->range(valor_inicial, valor_final)

OBS: O valor final não é inclusive
"""
for numero in range(1, 10+1):
    print(numero, end="")

#Exemplo 4 de for:
for indice, valor in enumerate(nome):
    print(nome[indice])

#Exemplo 5 de for:
#Exclusão de um valor com "_" poís 
#não precisamos de tal valor

for _,letra in  enumerate(nome):
    print(letra)

#Exemplo 6 de for:

#Seleção entre index ou letra
for valor in enumerate(nome):
    print(valor)

