"""
POO - Heranca multipla

OBS ->  A herança multipla pode ser feita de duas maneiras
    - Por multiderivação direta
    - Por multiderivação Indireta



# Exemplo 1 - Multiderivação direta

class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class MultiDerivada(Base1, Base2, Base3):
    pass

# Exemplo 2 - Multiderivação indireta

class Base1:
    pass
class Base2(Base1):
    pass
class Base3(Base2):
    pass

class MultiDerivada(Base3):
    pass

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

class Pinguin(Terrestre,Aquatico):

    def __init__(self,nome):
        super().__init__(nome)

# Testando


tux = Pinguin('Pingo')
print(tux.nadar())
print(tux.cumprimentar())
print(tux.andar())
print(tux.cumprimentar()) # Method Resolution Order - MRO

