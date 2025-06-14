"""
MIn e Max

max() ->Retorna maior valor de um iterável de


lista = [1,8,4,99,34,129]
print(max(lista))

dicionario = {"a":1,'b':8,'c':4,'d':99,'e':34,'f':129}
print(max(dicionario)) # f

dicionario = {"a":1,'b':8,'c':4,'d':99,'e':34,'f':129}
print(max(dicionario.values())) #129


lista = [1,8,4,99,34,129]
print(max(lista))

dicionario = {"a":1,'b':8,'c':4,'d':99,'e':34,'f':129}
print(max(dicionario)) # f

dicionario = {"a":1,'b':8,'c':4,'d':99,'e':34,'f':129}
print(max(dicionario.values())) #129

# Faça um programa que mostre dois valores do usuário e mostre o maior

num1 = int(input(print("Digite um número: ")))
num2 = int(input(print("Digite um número: ")))

print(max(num1,num2))
print('a','bc','def','ghij')

min -> retorna o menor valor em um iterável ou o menor


lista = [1,8,4,99,34,129]
print(max(lista))

dicionario = {"a":1,'b':8,'c':4,'d':99,'e':34,'f':129}
print(max(dicionario)) # f

dicionario = {"a":1,'b':8,'c':4,'d':99,'e':34,'f':129}
print(max(dicionario.values())) #129


lista = [1,8,4,99,34,129]
print(max(lista))

dicionario = {"a":1,'b':8,'c':4,'d':99,'e':34,'f':129}
print(max(dicionario)) # f

dicionario = {"a":1,'b':8,'c':4,'d':99,'e':34,'f':129}
print(max(dicionario.values())) #129

# Faça um programa que mostre dois valores do usuário e mostre o maior

num1 = int(input(print("Digite um número: ")))
num2 = int(input(print("Digite um número: ")))

print(max(num1,num2))
print('a','bc','def','ghij')


nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Olivander']

print(max(nomes))
print(min(nomes))

print(max(nomes, key = lambda nome: len(nome)))
print(min(nomes, key = lambda nome: len(nome)))

"""

musicas = [
    {'Titulo': 'pão', 'tocou': 3},
    {'Titulo': 'ovo', 'tocou': 2},
    {'Titulo': 'cheetos', 'tocou': 4},
    {'Titulo': 'pedra', 'tocou': 32},
]
print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# Desafio!

print(max(musicas, key=lambda musica: musica['tocou']) ['titulo'])
print(min(musicas, key=lambda musica: musica['tocou']) ['titulo'])

# DESAFIO!
max = 0
for musica in musicas:
        if musica ['Tocou'] > max:
            max = musica['tocou']
for musica in musica:
    if musica ['tocou'] == max:
        print(musica['titulo'])

min = 99999
for musica in musica:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])