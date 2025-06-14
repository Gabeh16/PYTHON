"""
Estruturas lógicas: and, or, not, is

operadores unários
    -not, is
operadores binários
    -and, or
"""

ativo = True
logado = False

#OPERADOR UNÁRIO
if ativo and logado:
    print("Bem-vindo usuário")
else:
    print("Você precisa ativar sua conta")
#OPERADOR BINÁRIO
if not ativo:
    print("Você precisa ativar sua conta")
else:
    print("bem vindo usuário")

if logado is True:
    print("Olá")
else:
    print("Tente novamente")

#Ativo é falso?
print(ativo is True)