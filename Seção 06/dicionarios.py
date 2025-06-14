"""
Dicionários

São coleções do tipo chave/valor

- São representados por chaves {}

 print(type({}))

OBS: Sobre dicionários
    - Chave e valor são separados por ":"
    - Chave ou valor pode ser qualquer dado
    - Podemos misturar os dados

# Criação de diconários

# Forma 1 (mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos' }

print(paises)
print(type(paises))

# Forma 2 (Menos comum)

paiises = dict(br='Brasil', eua='Estados Unidos')

# Acessando elementos

# Forma 1 - Acessando via chave

print(paises['br'])
print(paises['eua'])

# Forma 2 - Acessando via get (Recomendado)

print(paises.get('br'))
print(paises.get('eua'))
print(paises.get('none'))

# Descobrindo se o dicionário possui algum valor

print('br' in paises)
print('eua' in paises)
print('ru' in  paises)

if 'ru' in paises:
    russia = paises('ru')

# Podemos utilizar qualquer tipo de dado

localidades = {
    (31.000,36.000): "Escritorio em Tókio"
}

# Adicionar elementos em um dicionário

receita = {'jan': 100,'fev':120, 'mar':130}

print(receita)
print(type(receita))

# Forma 1

receita['abr'] = 300
print(receita)


# Forma 2

novo_dado = {'mai':500}

receita.update(novo_dado)
print(receita)

receita ['jun'] = 420
receita ['jul'] = 510
receita ['ago'] = 620
receita ['set'] = 740
print(receita)

# Atualizando dados em um dicionário

# Forma 1
receita['abr'] = 400

print(receita)

# Forma 2
receita.update({'abr': 320})

print(receita)

# Remover dados de um dicionário

receita = {'jan': 100,'fev':120, 'mar':130}

print(receita)
# Forma 1 - Mais comum
ret = receita.pop('mar')
print(ret)
# OBS: Sempre informar a chave para não dar erro
# OBS: Remove e retorna o valor

# Forma 2

del receita ['fev']
print(receita)

# OBS: Valor não vai ser retornado

# Imagine que você tem um comércio eletronico


Carrinho de compra:
    produto 1
    - Nome
    - Quantidade
    - Preço
    produto 2
    - nome
    - Quantidade
    - Preço


# 1 - Poderiamos utilizar uma lista para isso? sim
carrinho = []

produto1 = ['Playstation 4',1, 230.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriamos que saber o indice de cada informação

# 2 - Podemos utilizar uma Tupla para isso? Sim

produto1 = ('Playstation 4',1, 230.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1,produto2)

# 3 - podemos usar um dicionário  para isso? Sim

carrinho = []

produto1 = {'nome':'playstation 4','Quantidade': 1, "Preço":23000}
produto2 = {'nome': 'God of War 4', 'Quantidade': 1, "Preço": 45000}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma adicionamos e removemos de forma fácil e rápida
# E podemos também ter a certeza sobre toda informação

# Limpar o dicionário
 d.clear()
 print(d)

 # Copiando um dicionário para outro

# Forma 1 - Deep Copy

novo = d.copy()

print(novo)

novo['d'] = 4

print(d)
print(type(d))

# Forma 2 - Shallow Copy

novo = d
print(d)
novo ['d'] = 4

print(d)
print(novo)

dicio = {'nome': 'Gabriel Costa', 'idade':32, 'hetero': True}
"""

dicio = {'nome': 'Gabriel Costa', 'idade':32, 'hetero': True}

