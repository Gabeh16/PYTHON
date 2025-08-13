"""
Preservando metadatas com wraps

metadata -> Dados intrinsecos em arquivos.

wraps -> sao funcoes que envolvem elementos com diversas fin


def ver_log(funcao):
    def logar(*args,**kwargs):
        print(f"Chamando {funcao.__name__}")
        print(f"Aqui a documentacao: {funcao.__doc__}")
        return funcao (*args, **kwargs)
    return logar

@ver_log
def soma(a,b):
    return a+b

print(soma.__name__)
print(soma.__doc__)
"""

from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args,**kwargs):
        print(f"Chamando {funcao.__name__}")
        print(f"Aqui a documentacao: {funcao.__doc__}")
        return funcao (*args, **kwargs)
    return logar

@ver_log
def soma(a,b):
    return a+b


#print(soma.__name__)
#print(soma.__doc__)

print(help(soma))