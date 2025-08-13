"""

-> objetos são intancias da classe, apos o mapeamento do objeto do mundo real para sua
representacao computacionaldevemos poder criar quantos objetos forem necessarios


#Instancias / objetos

lamp1 = Lampada('branca',110,60)

lamp1.ligar_desligar()
lamp1.ligar_desligar()

print(f'A lampada esta ligada {lamp1.checa_lampada()}')

cc1 = ContaCorrente(5000,20000)

user1 = Usuario("MAnga ","Afonso",'manga34@gmail.com','1090')

"""

class Lampada:
    def __init__(self,cor,voltagem,luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False # Toda lampada sempre sera falsa.

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True
class Cliente:
    def __init__(self,nome,cpf):
        self.__nome = nome
        self.__cpf = cpf
    def diz(self):
        print(f'O cliente {self.__nome} diz oi')

class ContaCorrente:

    contador = 4999

    def __init__(self,limite,saldo,cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero
    def mostra_cliente(self):
        print(f'O cliente e {self.__cliente.Cliente__nome}')



class Usuario:
    def __init__(self,nome,sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


clien = Cliente('Cleiton thompson', '123.456.456.78' )

cc = ContaCorrente(5000,10000,clien)

print(cc.mostra_cliente())
