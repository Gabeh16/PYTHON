"""
Generators

Tuple comprehension / Generators


# Utilizando Generators
nomes= ["Carlos", 'Cleiton', 'Claudio', 'Cristian','Roberto']

# Não é um list comprehension
print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension

res = [ nome[0] == 'C' for nome in nomes]
print(type(res))

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))


# Mostra quantos bytes a string 'geek' está ocupando em memória. Quanto maior a string mais espaço ocupa
print(getsizeof('Geek'))

print(getsizeof('UNiversity'))

print(getsizeof(9))

print(getsizeof(57))

print(getsizeof(9293441092836451))

print(getsizeof(True))


# Qual a utilidade de getsizeof()-> Retorna a quantidade de  bytes em memória do elemento passado como parâmetro
from sys import getsizeof

# Gerando lista de numeros com list comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de numeros com set comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com dic comprehension
dic_comp = getsizeof({x: x * 10 for x in range (1000)})

# Gerando uma lista de números com generator
gen = getsizeof(x * 10 for x in range (1000))

print(list_comp)
print(set_comp)
print(dic_comp)
print(gen)
"""
# Eu posso iterar no generator expression

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)