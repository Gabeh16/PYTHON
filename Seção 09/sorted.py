"""
Sorted

Podemos utilizar o sorted() com qualquer iterável

O sorted sempre retorna uma lista

lista = [2,1,4,7,9,10,6,3,5,8]
print(lista.sort())

# Exemplo

numeros = [2,1,5,9]
print(numeros)

print(sorted(numeros)) # DO MENOR PARA O MAIOR
print(numeros)


numeros = [6,1,8,2]
print(numeros)

print(sorted(numeros))

# Adicionando parâmetros ao sorted()

print(sorted(numeros, reverse=True))# Ordena do maior para o menor


# Sorted para coisas mais complexas

usuarios = [
    {'username':'Samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username':'Carla', 'tweets': ['Eu adoro gatos']},
    {'username':'Diego', 'tweets': [], 'cor': 'Amarelo'},
    {'username':'Cleiton', 'tweets': []},
    {'username':'Afonso', 'tweets': ['Eu adoro cachorro', 'Vou sair hoje']},
    {'username':'Joel', 'tweets': [], 'cor': 'preto', 'musica':'Rock'}

]
print(usuarios)
# Ordenando pelo username - Ordem alfabetica
print(sorted(usuarios,key= lambda usuario: usuario['username'], reverse=True ))

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets']),reverse=True))


"""
# Ultimo exemplo

musicas = [
    {'Titulo': 'pão', 'tocou': 3},
    {'Titulo': 'ovo', 'tocou': 2},
    {'Titulo': 'cheetos', 'tocou': 4},
    {'Titulo': 'pedra', 'tocou': 32},
]

# Ordenar da menos tocada para a mais tocada
print(sorted(musicas, key = lambda musica: musica['tocou']))

# Ordenar da mais tocada para a menos tocada
print(sorted(musicas, key = lambda musica: musica['tocou'], reverse = True))