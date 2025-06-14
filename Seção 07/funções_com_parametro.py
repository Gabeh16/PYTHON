"""
Funções com parâmetro (de entrada)

- Funções que recebem dados para serem processados
dentro dela mesma

Se pensarmos em um programa qualquer sempre temos:

Entrada -> Processamento -> Saída

As funções que podem:

- Não ter entrada
- Não ter saida
- Possuem entrada, mas não possuem saida
- Não possuem entrada, mas possuem saida
- Possuem entrada e saida

# Refatorando uma função

def quadrado(numero):
    return numero * numero

print(quadrado(7))
print(quadrado(3))
print(quadrado(5))

print(quadrado())# TypeError

# Refatorando a função

def cantar_parabens(aniversariante):
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante} e')

cantar_parabens('Cleber')

# Funções podem ter n parametros de entrada e
Receber diversos parâmetros, São separados por
Virgula

# Exemplo

def soma(a,b):
    return a + b

print(soma(2,5))
print(soma(10,20))

def multiplica(num1, num2):
    return num1 * num2

print(multiplica(2, 8))
print(multiplica(5,5))

def mais(num1, num2, num3):
    return num1 + num2 + num3

print(mais(10,21,11))
print(mais(12,53,11))

def outra(num1, b, msg):
    return (num1 + b) * msg

print(outra(5,5,2))
print(outra(1,1,25))

print(outra(2,5,'Geek'))
print(outra(6,4,'Python'))

# Parametros e Argumentos
def parametro_argumento(number1): # Parametro
    return number1

print(parametro_argumento(6))# Argumento do Parametro

# Dois parâmetros com o Print
def arg(num2,num3):
    print(f'Seus números escolhidos é {num2} e {num3}')
arg(3,5)


# Nomeando Parâmetros

def nome_completo(nome,sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'
print(nome_completo('Ângelo','Júlio'))

# A diferença entre Parâmetros e Argumentos

# Parâmetros são variáveis declaradas na definição de um função
# Argumentos são dados passados durante a execução de uma função

# A ordem dos parâmetros importa

nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados(KeyWord Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos
# Para informa-lós, podemos utilizar qualquer ordem

print(nome_completo(nome='Angelina', sobrenome= 'Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))

# Erro comum na utilização do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total # Localização errada do RETURN
lista= [1,2,3,4,5,6,7]
print(soma_impares(lista))

tupla = 1,2,3,4,5,6
print(soma_impares(tupla))
print(type(tupla))
"""
