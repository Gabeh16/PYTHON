"""
Conjuntos

- Conjuntos em qualquer linguagem de programação,
fazemos referência á teoria dos conjuntos da matematica

- No Python se chama de SETS(conjuntos)

- Sets não possuem valores duplicados
- Sets não possuem valores ordenados
- Elementos não são acessados via indice
- Conjuntos não são indexados

Diferença entre conjuntos e mapas
    - Um dicionário tem chave/valor:
    - Um conjuntos tem apenas valor:

# Definindo um conjunto:

# Forma 1

s = set ({1, 2, 3, 4, 5, 6, 7, 8, 9})

print(s)
print(type(s))

#OBS: Ao criar um conjunto se tiver valores iguais um será ignorado

# Forma 2 - Mais comum

s = {1,2,3,4,5}

print(s)
print(type(s))

tupla = (1,23,4,5,6,77,85,89)

s2 = {tupla}
print(s2)

# Aceita vários tipos de dados
s = {1,"b", True,34.4, 44}
print(s)


# Exemplo com conjuntos, contando com "set"

lista1 = [1,2,2,3,4,5,6,6,5,6,8,9,9,10,11,10]
print(lista1)
print(len(lista1))

# Preciso saber quantas são sem duplicação

# Basta usar o set para

print(len(set(lista1)))

# Adicionando  elementos em um conjunto

s = {1,2,3}
s.add(4)

print(s)

# Removendo elementos

# Forma 1

s.remove(3)
print(s)

# Forma 2

s.discard(2)
print(s)
# OBS: Não apresenta erros

# Copiando um conjunto para outro

# Forma 1 - Deep Copy

conjunto = {1,2,3,4}
print(conjunto)
novo = conjunto.copy()

novo.add(5)
print(novo)

# Forma 2 - Shallow Copy

s = {1,2,3}

novo = s
novo.add(4)

print(novo)
print(type(novo))

"""
# apagar itens de um conjunto

s = {1,2,2,3}
s.clear()
print(s)
