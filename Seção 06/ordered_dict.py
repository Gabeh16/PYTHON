"""
Modulo collections - Ordered Dict

# Em um dicionário  a ordem dos elementos não é garantida

dicionario = {'a':1, 'b':2, 'c':3 ,'d':4 ,'e':5}

for chave,valor in dicionario.items():
    print(f"Chave = {chave} e Valor = {valor}")

# Testando um dicionário ordenado
from collections import OrderedDict

dicionario = OrderedDict({'a':1, 'b':2, 'c':3 ,'d':4 ,'e':5})

for chave,valor in dicionario.items():
    print(f"Chave = {chave} Valor = {valor}")
"""
from collections import OrderedDict

# Entendendo a diferença entre dict e ordered dict

# Dicionários comuns

dict1 = {'a': 1, 'b': 2}

dict2 = {'a': 2, 'b': 1}

print(dict1 == dict2) # True -> Pois a ordem não importa para dicionario comum

# Ordered dict

odict1 = OrderedDict({'a': 1, 'b': 2})

odict2 = OrderedDict({'a': 2, 'b':1})

print(odict1 == odict2) # False -> Pois a ordem dos elementos faz diferença para o OrderedDict