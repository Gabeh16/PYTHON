"""
POO - Abstracao e encapsulamento

Encapsular -> Capsula


Abstração -> é o ato de expor apenas dados relevantes de uma classe, escondendo atributos
e metodos privados do usuario.


print(conta1.__dict__)

conta1.extrato()

print(conta1.__dict__)

conta1.depositar(150)

print(conta1.__dict__)

conta1.sacar(200)

print(conta1.__dict__)

valor = 100

conta2.sacar(valor)

conta1.depositar(valor)

"""
class Conta:
    contador = 400

    def __init__(self,titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self,valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print('Saldo insuficiente')

    def transferir(self,valor,conta_destino):
        # 1 Remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10

        conta_destino.__saldo += valor


# Testando

conta1 = Conta('Geek',150,1500)
conta1.extrato()

conta2 = Conta('Felicity',300, 2000)
conta2.extrato()

conta2.transferir(100,conta1)

conta1.extrato()
conta2.extrato()
