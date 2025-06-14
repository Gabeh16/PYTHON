"""
Funções com Parâmetro padrão (Defaul paramters)

- Funções onde a passagem de parâmetro seja opcional

# Exemplo de função onde a passagem de parâmetro seja
opcional
print('Geek University')

# Parâmetro obrigatório

def quadrado(numero):
    return numero ** 2
print(quadrado(3))
print(quadrado()) #TypeError

def exponencial (numero,potencia=2):
    return numero ** potencia
print(exponencial(2,3))# 2 * 2 * 2
print(exponencial(3,2))# 3 * 3

print(exponencial(3))# Por padrão eleve ao quadrado
print(exponencial(3, 5)) # Eleva à potencia informada pelo usuário


OBS:
# Se o usuário passar somente 1 argumento, este será
atribuido ao parâmetro numero, e será calculado o
quadrado deste número:

# Se o usuario passar 2 argumentos, oprimeiro será
atribuido ao parâmetro número e o segundo ao parâmetro
potência, então será calculada essa potênocia.

# ERRO
def teste(p1=2,p2):
    return p1 ** p2
print(teste())

# Outros Exemplos

def soma(num1=5, num2=4):
    return num1 + num2

print(soma(4,3))
print(soma(4)) # TypeError
print(soma())  # TypeError

# Exemplo mais complexo

def mostra_informação(nome='Geek', instrutor= False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'

print(mostra_informação())
print(mostra_informação(instrutor=True))
print(mostra_informação(True))
print(mostra_informação('Ozzy'))
print(mostra_informação(nome='Stephany'))

# Por quê utilizar parâmetros com valor padrão

- Maior flexibilidade nas funções
- Evita erros com parâmetros incorretos
- Nos permite trabalhar com exemplos mais légiveis de código

# Quais tipos de dados podemos utilizar com valores default
para parâmetro

- Qualquer tipo de dado:
# Exemplos

def soma (num1, num2):
    return a+b

def mat (num1,num2,fun=soma):
    return fun(num1, num2)

def subtracao(num1,num2):
    return num1 - num2

print(mat(2,3))
print(mat(2,3,subtracao()))

# Escopo - Evitar problemas e confunsões

# Variáveis Globais
# Variáveis Locais

instrutor = 'Geek' # Variavel Global

def diz_oi():
    instrutor = 'Python' # Variável Local
    return f'Oi {instrutor}'
print(diz_oi())

#OBS: Se ambas forem iguais a local terá prioridade
"""
# Atenção com variáveis globais

total = 0

def teste():
    global total # Avisando sobre o uso da var global
    total = total + 1
    return total

print(teste())
print(teste())
print(teste())

# Funções declradas dentro de funções
# -> Tendo uma forma especial de escopo de variavel

def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())