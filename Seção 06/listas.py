"""
Listas

listas em python funcionam como vetores (arrays)
em outras linguagens, com a diferença de serem dinâmicos
e também de poder colocar qualquer tipo de dado

em Python

-Dinâmico: não possui tamanho fixo: ou seja
podemos criar a lista e simplesmente ir adicionando
elementos
-Qualquer tipo de dado: Não possuem tipo de dado fixo:
podemos por qualquer tipo de dado

As listas ficam entre colchetes


type([])

lista1 = [1,2,3,4,55,66,11,22,33,44,90]
lista2 = ["g","a","b","r","i","e","l","d","i","a"]
lista3 = []

lista4 = list(range(11))

lista5 = list("Geek University")

#Podemos checar se determinado valor está na lista
num = 18
if num in lista4:
    print(f"Encontrei o número {num}")
else:
    print(f"Não encontrei o número oito {num}")

if "g" in lista2:
    print("Encontrei a letra")
else:
    print("Não encontrei")

#Podemos facilmente ordenar a lista
lista1.sort()
print(lista1)

#Podemos contar o número de ocorrências de um valor em uma lista
print(lista2.count("a"))
print(lista5.count("e"))

#Adiconar elementos em listas
print(lista1)
lista1.append(42)
#Adiciona apenas um valor por vez
print(lista1)

lista1.append([87,98,34])#Elemento unico
print(lista1)
if [87,98,34] in lista1:
    print('encontrei a lista')
else:
    print("Não encontrei a lista")

#Extensão da lista

lista1.extend([12,33,42])

#Inserindo valor pelo INDEX
#Inserimos um novo valor com posição definida

lista1.insert(2,"Novo valor")
print(lista1)

#Unindo duas listas
lista6 = lista1 + lista2
print(lista6)

# Invertendo Lista

# Forma1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma2
print(lista1[::-1])
print(lista2[::-1])

#Copiar uma lista
lista6 = lista1.copy()
print(lista6)


# Contar elementos em uma lista
print(len(lista1))


# Remover o último elemento
print(lista5)
lista5.pop()

# Remover objetos pelo indice
# OBS: Os elementos na direita deste index vão para à esquerda
lista5.pop(4)

# Apaga tudo da lista
print(lista5)
lista5.clear()
print(lista5)


# Convertendo uma String em uma lista
curso = "Programação em Python: Essencial"
print(curso)
curso = curso.split()
print(curso)

# Corvertendo uma lista em String
lista6 = ["Programação", "em", "Python"]
print(lista6)

curso = ' '.join(lista6)
print(curso)

# É possivel por qualquer valor mesmo em uma lista
lista6 = [1,34,True,"Geek", "d", [1,2,3], 3.4]

# Exemplo 1 - FOR

soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - WHILE

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto no carrinho ou digite sair para sair?")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

lista1 = [1,2,3,4,55,66,11,22,33,44,90]

lista2 = ["g","a","b","r","i","e","l","d","i","a"]

lista3 = []

lista4 = list(range(11))

lista5 = list("Geek University")

#Utilizando Variáveis em listas
numeros = [1,2,3,4,]

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Encontrar indice de um elemento na lista
numeros = [5, 6, 7, 6, 8, 9, 10]

# Em qual index da lista está o valor 6?
#Retorna o index do primeiro valor encontrado
print(numeros.index(6))

# Em qual index da lista está o valor 9?
print(numeros.index(9))

# Error - se apresentar valor que a lista não tem
print(numeros)

# Podemos fazer busca dentro de um range, ou seja, qual index começar a buscar
print(numeros.index(5,1))# INDEX 1
print(numeros.index(5,2))# INDEX 2
print(numeros.index(5,3))# INDEX 3

# Busca com range inicio/fim
print(numeros.index(8,3,6))

# Revisão de slicing

# lista(inicio:fim:passo)
# range(inicio:fim:passo)

# Trabalhando com slice de lista

lista = [1, 2, 3, 4]

print(lista[1:]) #Começa no 1 pega tudo

print(lista[:2]) #Parametro FIM so vai até o dois

print(lista[0:4:2]) #Parametro PASSO dois em dois

#Parametros de lista
lista = [1, 3, 4, 5, 6, 7, 7, 2, 3]

print(sum(lista)) #Soma da lista
print(max(lista)) #Maximo valor da lista
print(min(lista)) #Minimo valor da lista
print(len(lista)) #Tamanho da lista

# Criando tuplas
lista = [1,2,3,4,5,6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Copiando uma lista para outra

# Shallow copy e Deep copy

#Forma 1 - Deep Copy

lista = [1,2,3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)

print(lista)
print(nova)

# Uma lista não afeta a outra

# Forma 2 - Shallow copy

lista2 = [1,2,3]
print(lista2)

nova2 = lista

print(nova2)
nova2.append(4)

print(lista)
print(nova)

# Está cópia possui atribuição
"""
