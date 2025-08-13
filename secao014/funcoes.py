"""
funcoes de maior grandeza

- Quando uma linguagem, indica que podemos ter funcoes que retornam
outras funcoes como resultado ou mesmo que podemos passar
funcoes como argumentos para outras funcoes e ate mesmo criar variaveis
do tipo funcoes no meu programa.


# Exemplo - Definindo as funcoes

def somar(a,b):
    return a + b
def diminuir(a,b):
    return a - b
def multiplicar(a,b):
    return a * b
def dividir(a,b):
    return a / b
def calcular(num1,num2,funcao):
    return funcao(num1,num2)

# Testando

print(calcular(4,3, somar))

print(calcular(4,3,diminuir))

print(calcular(4,3, multiplicar))

print(calcular(4, 3, dividir))


# Funcoes

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice (('e ai', 'sai', 'gosto de você'))

    return humor() + pessoa

#testando

print(cumprimento('Angelina'))

print(cumprimento('Felicity'))


# Retornando funcoes de outras funcoes

from random import choice

def faz_me_rir():
    def rir():
        return choice(('HAHAHAHAHAHHAHAHA', 'KKKKKKKKKKKKK', 'YAYAYAYAYYAYAYA'))
    return rir

# Testando

rindo = faz_me_rir()
print(rindo())
"""
