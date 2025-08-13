"""
POO - Herança

-> reaproveitamento de codigos estendendo classes

OBS: Extender uma classe para herdar atributos e metodos da classe herdada

class Cliente:

    def __init__(self,nome, sobrenome,cpf, renda):
        self.__nome =nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Funcionario:
    def __init__(self,nome,sobrenome,cpf,matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

OBS: Quando uma classe herda algo de outra Classe ela herda TUDO


# CLASSE GENERICA
class Pessoa:

    def __init__(self,nome,sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):

    # Cliente Herda de Pessoa
    def __init__(self,nome,sobrenome,cpf, renda):

        # Metodo super() forma de ter acesso a meteodos e atributos da super classe
        super().__init__(nome, sobrenome, cpf)
        super().nome_completo()
        self.__renda = renda

class Funcionario(Pessoa):

    # Funcionario herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, matricula):

        # Metodo super() forma de ter acesso a meteodos e atributos da super classe
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

cliente1 = Cliente('Gabriel','Costa',55294369869,5000)
funcionario1 = Funcionario('Gabriel','Diares','534.265.786-90',2501810)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)

print(funcionario1.__dict__)

# Sobescrita de Métodos (Overriding)

-> Ocorre quando reescrevemos/reinplementamos  um metodo presente na super classse em classes filhas


# CLASSE GENERICA
class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):

    # Cliente Herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, renda):
        # Metodo super() forma de ter acesso a meteodos e atributos da super classe
        super().__init__(nome, sobrenome, cpf)
        super().nome_completo()
        self.__renda = renda


class Funcionario(Pessoa):

    # Funcionario herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, matricula):
        # Metodo super() forma de ter acesso a meteodos e atributos da super classe
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula



cliente1 = Cliente('Gabriel', 'Costa', 55294369869, 5000)
funcionario1 = Funcionario('Gabriel', 'Diares', '534.265.786-90', 2501810)

"""

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

@dataclass
class Funcionario(Pessoa):
    cargo: str
    salario: int

f = Funcionario( 'Gabriel Costa Diares', 19, 'Auxiliar de TI', 1800)

