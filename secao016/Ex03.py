"""
Criar uma classe ContaBancaria com saldo privado e métodos para depositar e sacar.

"""

class ContaBancaria:

    def __init__(self,saldo):

        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self,novo_saldo):
        self.__saldo = novo_saldo

    def depositar(self, deposito):
        return self.saldo + deposito

    def sacar(self,retirada):
        return self.saldo - retirada

    def saldo_atual(self):
        return

valor = ContaBancaria(900)

print(valor.depositar(800))
print(valor.sacar(500))
print(valor.depositar(200))
print(valor.sacar(500))