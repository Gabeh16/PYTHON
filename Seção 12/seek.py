"""
função para a movimentação do cursor

-> seek()

com ela eu posso escolher em que lugar o cursor deve voltar
e controlar sua movimentação

"""

arquivo = open('texto.text')

print(arquivo.read())

# Começa do zero de novo
arquivo.seek(0)

# Imprimi do zero agora
print(arquivo.read())

print(arquivo.closed)

arquivo.close()

print(arquivo.closed)

