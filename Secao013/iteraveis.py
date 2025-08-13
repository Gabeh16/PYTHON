"""
Iterator
-> Objeto que retorna dado

nome = 'Geek ' # Um iterable
numeros= [1,2,3,4,5,6,7,8,9]

it1 = iter(nome)
it2 = iter(numeros)


# O next serve para revelar um elemento por vez quando chamado

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
"""
nome = 'Geek'

for letra in nome:
    print(f'{letra}')