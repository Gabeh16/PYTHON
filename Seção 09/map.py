"""
Map

 - Mapeamento de valores para função.
 
 
import math


def area(r):
    ""Calcula a área de um circulo com raio 'r' ""
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))


raios = [1,2,3,4,5,6,7,89,9888]

# Forma Comum

areas = []
for r in raios:
    areas.append(area(r))
print(areas)

# Forma 2 - Map

areas = map(area, raios)
print(areas)
print(list(areas))

# Forma 3 - Map com Lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# Para fixar - Map

# Temos dados iteráveis:

# dados: a1,a2.....,an

# Temos uma função

# Função: f(x)

# Utilizamos a função map(f,dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função

# O Map Object: f(a1),f(a2),f(...), f(an)
"""