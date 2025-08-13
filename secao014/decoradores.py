"""
- Decoradores

Decorators -> São funções



# Decorator pattern

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args,**kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'olá, eu sou a/o {nome}'

@gritar
def ordenar(principal,acompanhamento):
    return f'Olá eu gostaria de {principal} acompanhado de {acompanhamento}'


print(saudacao('felix'))

print(ordenar ('picanha','batata frita'))

@gritar
def lol():
    return 'lol'

print(lol())
"""
#Decorator com argumentos

def verificar_primeiro_arguemnto(valor):
    def interna(funcao):
        def outra(*args,**kwargs):
            if args and args[0] !=valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor} '
            return funcao(*args,**kwargs)
        return outra
    return interna

@verificar_primeiro_arguemnto('pizza')
def comida_favorita(*args):
    print(args)

@verificar_primeiro_arguemnto(10)
def soma_dez(num1,num2):
    return num1 + num2

# Testando

print(soma_dez(10,12)) # 22

print(soma_dez(1,21)) # 22

print(comida_favorita("sanduiche",'pizza'))

