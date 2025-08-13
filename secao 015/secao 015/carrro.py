"""
Criar uma classe Carro com marca, modelo e ano.

Instanciar 3 carros diferentes e imprimir os atributos.

Criar um método ligar() que imprime "O carro está ligado".
"""
from dataclasses import dataclass


@dataclass
class Carro:
    marca: str
    modelo: str
    ano: int

    def ligar(self):
        print(f'O {self.modelo} está ligado')

    def idade(self):
        tempo = 2025 - self.ano
        print(f'Seu {self.modelo} tem {tempo} anos de idade')

carro1 = Carro(marca="Wolkswagen",modelo="Gol",ano= 2006)
carro2 = Carro(marca="Wolkswagen",modelo="Polo",ano=2009)
carro3 = Carro(marca="Fiat",modelo="Cronos",ano=2012)

carro1.ligar()
carro1.idade()
print(carro2)
print(carro3)


