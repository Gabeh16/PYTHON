"""
POO -> Classes

Em poo classes nada mais são do que modelos dos objetos do mundo real sendo represnetados

Classes -> podem conter atributos para conter suas caracteristicas

- Metodos(Funcões) -> Representam os comportamentos do objeto, ações do objeto

OBS: objetos que serao mapeados para classes se tornam entidades

"""

# Criando um tipo de dado

class Lampada: # Primeira letra sempre maiuscula por convenção
    pass

lamp = Lampada()

print(type(lamp))

# Usamos classes indiretamente

valor = int("42") # Cast

print(help(int))