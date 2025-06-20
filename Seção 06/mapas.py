"""
Mapas conhecidos como dicionários

Dicionários em Python são reconhecidos por {}

# Ierar sobre dicionários
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f"Em {chave} recebi R${receita[chave]}")

# Acessando as chaves
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores

print(receita.values())
for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários

for chave, valor in receita.items():
    print(f"chave {chave} e valor {valor}")

receita ={"jan": 100, 'fev': 200, "mar": 300}

# Soma. Maximo, Minimo e tamanho

# Se os valores forem inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
"""

receita ={"jan": 100, 'fev': 200, "mar": 300}

# Soma. Maximo, Minimo e tamanho

# Se os valores forem inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))