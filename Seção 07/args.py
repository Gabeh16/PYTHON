"""
Entendendo o "args"

- Args é um parâmetro, como outro qualquer,
poderia chmar de qualquer coisa desde que comece
com asterisco.

exemplo:

*xis

Mas por convenção, utilizamos *args para definir

Mas o que é o args?

O parâmetro args utilizado em uma função, coloca
os valores extras como entrada em uma tupla.
Tuplas são imutáveis

# Exemplos

def soma_todos_os_numeros(num1=1,num2=3,num3=2):
    return num1 + num2 + num3

print(soma_todos_os_numeros(4,6,9))

print(4,6)

# Entendendo o args
def soma_todos_numeros(nome,email,*args):
    return sum(args)

soma_todos_numeros('Joao', 'jota')
soma_todos_numeros('Joao', 'jota',1)
soma_todos_numeros('Joao', 'jota',2,3)
soma_todos_numeros('Joao', 'jota',2,3,4)
soma_todos_numeros('Joao', 'jota',3,4,5,6)

# Outro exemplo de utilização do args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem vindo Geek!'
    return 'Eu não tenho certeza quem você é'

print(verifica_info())
print(verifica_info(1,True,'University','Geek'))

def soma_todos_numeros(*args):
    return sum(args)
print(soma_todos_numeros())
print(soma_todos_numeros(3,4,5,6))

numeros = [1,2,3,4,5,6,7]

# Desempacotador
print(soma_todos_numeros(*numeros))

# Asterisco avisa o Python da lista e desempacota

"""
def comprar_pao(preco,temperatura,*args):
    return preco, temperatura, args

print(comprar_pao(10,'Quente','É necessário mais tempo no forno'))
