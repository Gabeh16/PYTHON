"""
Escrevevndo um iterador customizado

"""
class contador:
    def __init__(self,menor,maior):
        self.menor = menor
        self.maior = maior
# Transformando em iterable
    def __iter__(self):
        return self
    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor + 1
            return numero
        raise StopIteration


for n in contador(1,61):
    print(n)

for n in range(1,61):
    print(n)