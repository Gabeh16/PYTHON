"""
Filter

filter()-> Serve para filtrar dados de uma determinada
coleção

import statistics

# Dados coletados de um sensor
dados = [1,3,2.7,0.8,4.1,-0.1]

# Calculando dados utilizando mean()

media = statistics.mean(dados)

# Usando filter

res = filter(lambda valor:valor> media,dados)
print(list(res))

paises = ['','Argentina','','Brasil','Chile', '', 'Colombia','','Equador','','','Venezuela']

print(paises)

res = filter(lambda pais:len(pais) > 0 ,paises)
res = filter(None, paises)
res = filter(lambda pais: pais != '',paises)

print(list(res))


# Diferença entre map() e filter()

# map()-> Retorna valores novamente sem filtro
# filter()-> Retorna valores TRUE or FALSE
"""
# Exemplo mais complexo


usuarios = [
    {'username':'Samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username':'Carla', 'tweets': ['Eu adoro gatos']},
    {'username':'Diego', 'tweets': []},
    {'username':'Cleiton', 'tweets': []},
    {'username':'Afonso', 'tweets': ['Eu adoro cachorro', 'Vou sair hoje']},
    {'username':'Joel', 'tweets': []},
]
print(usuarios)

# Filtrar os usuários que estão inativos no Twitter

inativos = list(filter(lambda u: len(u['tweets']) ==0, usuarios ))
print(inativos)

# Combinar filter() e map()

nomes = ['Vanessa ', 'Ana', 'Maria']

# Devemos criar uma lista contendo

lista = list(map(lambda nome: f'sua instrutora é {nome}', filter(lambda nome: len(nome)< 5, nomes)))

print(lista)