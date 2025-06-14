"""
RAise -> Função embutida como DEF que serve para criarmos nossas exceções

# Exemplo real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser do tipo String')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser do tipo String')
    print(f'O texto "{texto}" será da cor {cor}')
colore("Geek",'Verde')

# Exemplo refatorado

def colore(texto, cor):
    cores = ('Verde','Azul','Amarelo','Branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser do tipo String')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser do tipo String')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto "{texto}" será da cor {cor}')

colore("Geek",'preto')
"""
# Exemplo real

def colore(texto, cor):
    cores = ('Verde','Azul','Amarelo','Branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser do tipo String')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser do tipo String')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto "{texto}" será da cor {cor}')

colore("Geek",'preto')