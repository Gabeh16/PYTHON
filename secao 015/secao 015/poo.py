"""
- POO é um paradigma de computação que usa de objetos do mundo real para o mapeamento
da linguagem computacional

- Paradigma de prorpriedades é a forma usada para criar sistemas

- Pirncipais elementos da orientacao a objetos

classe -> Modelo de obejto do mundo real sendo representado computacionalmente
atributo -> Caracteristicas do objeto
metodo -> Comportamento do objeto
construtor -> Método especial utilizado para criar os objetos
Objeto -> Intancia de classe

class Cliente:

    def __init__(self,nome,email):
        self.nome = nome
        self.email = email
    def exibir (self):
        print(self.nome,self.email)


guilherme = Cliente('Guilherme','email@gmail.com')

guilherme.exibir()

class Cliente:

    def __init__(self):
        pass

    def exibir(self):
        print('Eu sou um cliente')
    def chamar_exibir(self):
        self.exibir()

guilherme = Cliente()

guilherme.chamar_exibir()

"""
# Forma mais facil de criar Classes em python

from dataclasses import dataclass

@dataclass
class Cliente:
    nome:str
    email:str
    idade:int

    def exibir(self):
        print(
            f'Meu nome é {self.nome}, tenho {self.idade} anos e meu email é: {self.email}'
        )
gui = Cliente(nome = "Guilherrme", email = "gui@gmail.com", idade= "23")

gui.exibir()