"""
POO - > Atibutos

Atributos -> Igual a caracteristicas do objeto o que faz e como faz

Atributos

->Instancia
->Classe
->Dinamicos


- Instancia Atributos declarados dentro de um metodo construtor
    + Construtor: Metodo especial para formar um obj

class Acesso:
    def __init__(self,email,senha):
        self.email = email
        self.__senha = senha
    def mostrar_senha(self):
        print(self.__senha)
user = Acesso('user@gamil.com','123456')

print(user.email)
print(user.senha)

user.mostrar_senha()

# Atributos de Classe

class Produto:
    imposto = 1.05
    contador = 0 # Contagem constante de produtos
    def __init__(self, nome,descricao,valor):
        self.id = Produto.contador + 1 # Contagem de ID progressiva
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

p1 = Produto('Play 4', 'video game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

print(p1.valor) # Acesso possivel mas incorreto de atributo de classe
print(p2.valor)

# Acesso CORRETO

print(Produto.imposto) #CORRETO

print(p1.nome, end=', ')
print(p1.descricao, end=', ')
print(p1.valor, end=', ')
print(p1.id)
print(p2.id)
"""


class Lampada:
    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem # Dois UNDERSCORE serve para transformar essa variavel da classe em private
        self.__cor = cor
        self.__ligada = False

    @property
    def voltagem(self):
        return self.__voltagem
    @property
    def cor(self):
        return self.__cor
    @property
    def ligada(self):
        return self.__ligada

class ContaCorrente:
    def __init__(self,numero,limite,saldo):
        self.numero = numero
        self.limite = limite
        self.aldo = saldo

class Usuario:
    def __init__(self,nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Atributos de classe

class Produto:
    imposto = 1.05
    contador = 0 # Contagem constante de produtos
    def __init__(self, nome,descricao,valor):
        self.id = Produto.contador + 1 # Contagem de ID progressiva
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

# Atributo Dinâmico

# OBS: Exclusivo da instancia que o criou

p1 = Produto('Play 4','Video Game', 2300)

p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atb dinamico em tempo de execucao

p2.peso = '5kg'# AN classe atributo nao existe o atributo peso, Criado na hora

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')

print(p1,__dict__)

del p2.peso # Exclusao de forma dinamica 