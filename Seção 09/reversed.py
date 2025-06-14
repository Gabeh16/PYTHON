"""
Reversed

#Exemplo:

lista=[1,2,3,4,5]
res = reversed(lista)

print(res)
print(type(res))

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Conjunto/Set
print(set(reversed(lista)))

# Podemos iterar sobre o reversed

for letra in reversed('Gabriel Costa Diares'):
    print(letra, end='')

# Fazer o memso sem for

print(''.join(list(reversed('Geek university'))))

# Inverter com slice de strings
print('Texto FUlminante '[::-1])

# Podemos também usar o reversed para loop ao inverso
for n in reversed(range(0,10)):
    print(n)
# Inverso com range()
for ne in range(9,-1,-1):
    print(ne)
"""
