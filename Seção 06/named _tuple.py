"""
Modulo collections - Named Tuple

Named Tuple -> São tuplas diferentes, onde possui nome
e parâmetros especificos.
"""
from collections import namedtuple

# Precisamos definir o nome e parâmetro.

# Forma 1 - Declaração Named Tuple

cachorro1 = namedtuple('cachorro','idade raça nome')

# Forma 2 - Declaração Named tuple

cachorro2 = namedtuple('cachorro', 'idade','raça','nome')

# Forma 3 - Declaração Named tuple

cachorro3 = namedtuple('cachorro',['idade','raça','nome'])

# Usando

ray = cachorro3(idade=2, raça='chow-chow', nome='dog')
crow = cachorro3(idade=3, raça='PitBull', nome='Scooby')
print(ray)

# Acessando os dados


# Forma 2
print(ray.idade)
print(ray.raça)
print(ray.nome)

print(crow.idade)
print(crow.raça)
print(crow.nome)