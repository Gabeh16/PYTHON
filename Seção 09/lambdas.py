"""
Utilizando Lambdas

Conhecidas por Expressões lambdas, são funções
sem nome anônimas

# Função em Python
def funcao(x):
    return 3 * x + 1

print(funcao(5))

# Expressão Lambda
lambda x: 3 * x +1

# Utilizando lambda
nome = lambda x: 3 * x + 1

print(nome(4))
print(nome(7))

# Podemos ter lambdas com mais de um parâmetro

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('gabriel', 'costa'))



# Em funções Python podemos ter nenhuma ou várias entradas. Em lambdas também

amar = lambda: 'Como não amar Python'

uma = lambda x: 3 * x + 1

duas = lambda x, y: x + y

tres = lambda x,y,z: x+y+z

print(amar())
print(uma(5))
print(duas(4,90))
print(tres(2,3,87))


# Outro exemplo

autores = ['x xx zxx','xxx xx sxxx','xxx axxx','xxxxx cxxxx', 'xx xxx bxxxx']



autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)
"""

# Função quadrática
# f(x)= a * x ** 2 + b * x + c

# Definindo função

def gerando_funcao_quadratica(a,b,c):
    return lambda x: a * x ** 2 + b * x + c

teste = gerando_funcao_quadratica(2,3,4)

print(teste(0))
print(teste(1))
print(teste(2))

print(gerando_funcao_quadratica(3,0,1)(2))

var1 = lambda l,e,t,r,a: l + e + t + r + a
print(var1("a","c","a","b","o"))