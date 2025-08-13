"""
POO - Polimorfismo

OBjetos que podem se comportar de fromas diferentes

"""

class Animal:

    def __init__(self,nome):
        self.__nome = nome

    def falar(self):
        # Exceção
        raise NotImplementedError('A classe filha precisa implementar esse metodo')

    def comer(self):
        print(f'{self.__nome} está comendo...')

class Cachorro(Animal):

    def __init__(self,nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala uau uau')

class Gato(Animal):

    def __init__(self,nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau')

class Rato(Animal):

    def __init__(self,nome):

        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala squeak')



# testes

felix = Gato('Felix')
felix.comer()
felix.falar()

pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()

mickey = Rato('Mickey')
mickey.comer()
mickey.falar()
   