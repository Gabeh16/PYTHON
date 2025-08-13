"""
Crie a classe Carro que herda a classe veiculo e possui o atributo portas. Crie as propriedades
getters e setters para o atributo. Crie também o construtor da classe. Sobrescreva o metodo de imprimir
os dados do veiculo de forma a apresentar também a quantidade de portas do carro

"""

from Ex01 import Veiculo

class Carro(Veiculo):

    def __init__(self,portas,marca,modelo):
        super().__init__(marca,modelo)
        self.__portas = portas


    def imprimir(self):
        print(f'Dados do veiculo Marca {self.marca}, Modelo {self.modelo}, {self.portas} Portas')

    @property
    def portas(self):
        return self.__portas

    @portas.setter
    def portas(self, novas_portas):
        self.__portas = novas_portas

c1 = Carro('4','Wolkswagen','Polo')

c1.imprimir()