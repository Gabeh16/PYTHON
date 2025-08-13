"""
Crie a classe Veiculo, maraca e modelo. Crie as propriedades getters e setters para os atributos e um
metodo para imprimir os dados de um veiculo. Crie também o construtor da classe

"""



class Veiculo:

    def __init__(self,marca,modelo):

        self.__marca = marca
        self.__modelo = modelo

    def imprimir(self):
        print(f'Dados do veiculo Marca {self.__marca} Modelo {self.__modelo}')

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @marca.setter
    def marca(self,nova_marca):
        self.__marca = nova_marca

    @modelo.setter
    def modelo(self,novo_modelo):
        self.__modelo = novo_modelo

v1 = Veiculo('Fiat','Toro')
v2 = Veiculo('Wolkswagen','Polo')

v1.imprimir()
v2.imprimir()


