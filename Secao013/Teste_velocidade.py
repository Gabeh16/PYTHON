"""
Teste de velocidade com expressões geradoras

# Genarators (Geradores)
def nums():
    for num in range(1,10):
        yield num

ge1 = nums()

print(ge1) #Genrator

print(next(ge1))
print(next(ge1))

# Generator Expression

ge2 = (num for num in range(1,10))

print(next(ge2))
print(next(ge2))
"""
# Realizando o teste de velocidade

import time

# Generator expression

gen_inicio = time.time()
print(sum(num for num in range(1000000000)))
gen_tempo = time.time() - gen_inicio

#list Comprehension

list_inicio = time.time()
print(sum([num for num in range(100000000000)]))
list_tempo = time.time() - list_inicio

print(f'Generator expression levou{gen_tempo}')
print(f'List Comprehension levou {list_tempo}')
