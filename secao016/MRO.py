"""
POO - Method Resolution order MRO

Ordem de execução dos metodos

"""

class Animal:

    def __init__(self,nome):
        self.__nome = nome
    def cumprimentar(self):
        return f'Eu sou {self.__nome}'

class Aquatico(Animal):

    def __init__(self,nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadand'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar '

class Terrestre(Animal):

    def __init__(self,nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra'

class Pinguin(Terrestre, Aquatico):

    def __init__(self,nome):
        super().__init__(nome)

# Testando


tux = Pinguin('Pingo')
print(tux.cumprimentar()) # Method Resolution Order - MRO