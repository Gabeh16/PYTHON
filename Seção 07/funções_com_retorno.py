"""
Funções com retorno

# Exemplo função

numeros = [1,2,3]

ret_pop = numeros.pop()

print(f'retorno de pop{ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')

OBS: Funções que retornam valores, devem retornar
estes valores com a palavra reservada return

OBS: Não precisamos criar uma variável para receber
o retorno de uma função. Podemos passar a execução
da função para outras funções

# Vamos refatorar esta função para que ela retorne o valor

def quadrado_de_7():
    return 7 * 7 # Usando o RETURN

# Criamos uma variável para receber o retorno da função

ret = quadrado_de_7()
print(f"Retorno: {ret}")

# Podemos realizar operações dentro do PRINT
print(f"Retorno: {quadrado_de_7() + 1}")

# Treinando Funções

def diz_oi():
    print("Oi")
def diz_tchau():
    print('Tchau')
def diz_bem_vindo():
    print('Bem-Vindo')

diz_oi()
diz_tchau()
diz_bem_vindo()

def diz_ola():
    return 'Olá'
def diz_falou():
    return 'Falou'
def diz_fica_de_boa():
    return 'Fica de boa'

print(diz_ola())
print(diz_falou())
print(diz_fica_de_boa())
for n in range(3):
    diz_ola()
    diz_falou()
    diz_fica_de_boa()

# Refatorando  a primeira função

def diz_oi():
    return "Oi"

alguem = "Pedro"
print(diz_oi() +  alguem)

OBS: Sobre a palavra reservada return

1 - Ela finaliza a função, ou seja, ela sai da
execução da função;
# Exemplo (1)

def diz_oi():
    print("Estou sendo executado antes do Return")
    return 'Oi'
    print("Nunca serei executado após o return")

print(diz_oi())

2 - Podemos ter, diferentes returns em um função;

# Exemplo 2

# Três returns, porém apenas um funciona!
def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'
print(nova_funcao());

3 - Podemos em uma função retornar qualquer tipo de
dado e até mesmo multiplos valores;

# Exemplo 3

def outra_funcao():
    return 1,2,3,4,5

# num1,num2,num3,num4 = outra_funcao():
#print(num1,num2,num3,num4)

print(outra_funcao())
print(type(outra_funcao()))

# Vamos criar um cara ou coroa

from random import random

def joga_moeda():
    # Gera numeros pseudo-aleatório entre 1 e 0
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'
print(joga_moeda())
"""
# Erros comuns no uso de retorno, que é codificação desnecessária

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False
print(eh_impar())