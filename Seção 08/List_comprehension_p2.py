"""
List comprehension

Nós podemos adicionar estruturas condicionais logicas
às nossas list comprehension
"""

# 1

numeros = [1,2,3,4,5,6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 !=0]

print(pares)
print(impares)

# Refatorar

# Qualquer numero par modulo de 2 é 0 e 0 é false em python
pares = [numero for numero in numeros if not numero % 2]

impares = [numero for numero in numeros if numero % 2]

# 2

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
