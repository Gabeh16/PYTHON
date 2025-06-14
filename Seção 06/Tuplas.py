"""
Tuplas (tuple)

Tuplas são parecidas com listas

Existem duas diferenças básicas:

1 - São representados por parenteses ()

2 - As tuplas são imutáveis: Que ao se criar uma
tupla ela não muda

# Forma de se usar a TUPLA
print(type(()))

# OBS: As tuplas são representadas por ()

tupla1 = (1,2,3,4,5,6)
print(tupla1)

print(type(tupla1))
# Sem parenteses
tupla2 = 1,2,3,4,5,6
print(tupla2)

print(type(tupla2))

# Cuidado: Tuplas com 1 elemento

tupla3 = (4) # Isso não é tupla
print(tupla3)

print(type(tupla3))

tupla4 = (4,) # Isso é uma tupla
print(tupla4)

tupla5 = 4,
print(tupla5)

print(type(tupla5))

(4)-> Não é tupla
(4,)-> É tupla
4, -> É

# Criando tupla com range
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla

tupla = ('Geek Univeersity', 'Programação Python')

escola, curso = tupla

print(escola)
print(curso)

# Gera erro se colocar um número diferente de elementos para desempacotar

# Concatenação de tuplas
tupla1 = (1,2,3)
print(tupla1)

tupla2 = (4,5,6)
print(tupla2)

print(tupla1 + tupla2) # Imutáveis

print(tupla1)
print(tupla2)

# Verificar se determinado elemento está contido na tupla
tupla = (1,2,3)

print(3 in tupla)

# Iterando sobre uma tupla

tupla = (1,2,3)

for n in tupla:
    print(n)

for indice,valor in enumerate(tupla):
    print(indice,valor)

# Contando elementos dentro de uma tupla

tupla = ('a','b','c','d','e','a','b')

print(tupla.count('b'))

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))

# Dicas na utilização de tuplas

# Devemos usar tuplas SEMPRE que não precisar modificar dados em uma coleção

#Exemplo 1

meses = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

meses1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Slicing

# tupla(inicio:fim:passo)
print(meses[5:12:2])

# Acesso de elementos de uma tupla é semelhante a lista

print(meses[5])

i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificação em qual indice um elemento está na tupla

print(meses.index(1, 3 ))

# Por quê usar TUPLAS?

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam o código mais seguro
# * Trabalhar com um elemento imutável é mais seguro

# Copiando uma tupla para outra

tupla = (1,2,3)
print(tupla)

nova = tupla # Na tupla não temos SHALLOW COPY

print(nova)
print(tupla)

outra = (4,5,6)

nova = nova + outra

print(nova)
print(tupla)
"""
