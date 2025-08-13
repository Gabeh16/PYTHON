"""
Geradores
-> Geradores são iteradores:

OBS: mas nem sempre todo iterator é um generator

- Genrators podem ser criados com funcoes geradoras
- Funcoes geradoras utilizam a palavra reservada yield
- Generators podem ser criados com expressoes Geradoras

gen = conta_at(5)

print(next(gen))
print(next(gen))
print(next(gen))

for num in gen:
    print(num)
"""
# Exemplo de function generator
def conta_at(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

gen = conta_at(10)

print(next(gen))

print('Geek')

for num in gen:
    print(num)