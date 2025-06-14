"""
Tipo Booleano
-Algebra Booleana
-Duas constantes True ou False

True -> Verdadeiro
False -> Falso

OBS: sempre começa com letra maiúscula
"""
from idlelib.autocomplete import TRY_A

ativo = True

print(ativo)
"""
Operações básicas:
"""
# Negação (not):
"""
Fazendo a negação se o valor for verdadeiro o resultado
será falso, se for falso será verdadeiro. Ou seja
sempre o contrário.
"""
print(not ativo)

logado = False

#Ou (or):
"""
    Ou um ou outro deve ser verdadeiro 
True or True -> True
True or False -> True
False or True -> True
False or True -> False
"""
print(ativo or logado)

presente = True

# E (and):
"""
Também é uma operação binária, depende de dois
valores e ambos devem ser verdadeiros.

True and True -> True
True and False -> False 
False and True -> False 
False and False -> False
"""
print (ativo and logado and presente)