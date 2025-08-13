"""
Metodos -> Funcoes representa os comportamentos do objeto

Existem dois grupos de Metodos

- Metodos de instancias e metodos de classe

# METODO DE INSTANCIA


 ->Metodos magicos (DUNDER) Double underrline __xxx__

 # O que nao deve ser feito
def __correr__(self,metros): O que nao ser feito
    print(f'{self.__nome}')


p1 = Produto("play 4","Video Game",2300)

print(p1.desconto(50))

print(Produto.desconto(p1,40)) # self e desconto

user1 = Usuario("Calyton","Silva","Clay@gmail.com","Clay123#")
user2 = Usuario("Cleide","Souza","Clei@gmail.com","Clei123#")

print(user1.nome_completo())

print(user2.nome_completo())

print(Usuario.nome_completo(user1))

# Métodos de Classe

user = Usuario('Felicity', 'Jones','Felicity@gmail.com','12345')

Usuario.conta_usuario() # Forma correta
user.conta_usuario() # Forma possivel, mas incorreta

user = Usuario('Felicity','Jones','Felicirty@gamil.com','12345')

print(user.Usuario__gera_usuario()) # Acesso ruim

"""


class Lampada:
    def __init__(self,cor,voltagem,luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade

class ContaCorrente:

    contador = 4999

    def __init__(self,numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:

    contador = 0

    def __init__(self,nome,descricao,valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id
    def desconto(self, porcentagem):
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:

    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(f"Temos {cls.contador} usuários no sistema ")
    @classmethod
    def ver(cls):
        print('Teste')
    @staticmethod
    def definicao():
        return 'URX344'

    def __init__(self,nome,sobrenome,email,senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def __gera_usuario(self):
        return self.__email.split('0')[0]


# metodo estatico

print(Usuario.contador)

print(Usuario.definicao())

user = Usuario('Felicity','Jones','Felicity@gmail.com','1234')

print(user.contador)

print(user.definicao())
