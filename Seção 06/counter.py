"""
Modulo collections - Counter

Collections -> High-performance Container datatypes

Counter -> Recebe um iterável como parâmetro e cria um
objeto do tipo collections counter que é parecido com
um dicionário, contendo como chave o elemento da lista
passadacomo parametro e como valor a quantidade de
ocorrências desse elemento

# Utilizando Counter

from collections import Counter

# Podemos usar qualquer tipo de ITERÀVEL

lista = [1,1,1,1,1,2,2,2,2,3,3,3,3,44,4,4,4,4,5,5]

# Utilizando Counter
res = Counter(lista)

print(type(res))
print(res)

# Counter({1: 5, 2: 4, 3: 4, 4: 4, 5: 2, 44: 1})

# Para cada elemento ele criou uma CHAVE e VALOR

# Exemplo 2

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'u': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

# Exemplo 3

texto = ""seria interessante se houvesse algum
tipo de grupo para a troca da resolução dos
exercícios, ou ao menos dar alguma ajuda entre os
alunos.Tambem tenho alguns exercicios no qual
 não sei se há uma melhor forma para faze-los,
 vi que o professor disse que o aluno deve resolver
 cada exercicio individualmente ao inves de só
 querer procurar pelas respostas, o que há certo
 ponto faz sentido, porém muitas vezes acaba confundindo o aluno em certas situações.Voces não sentem falta de uma seção com a resolucao dos exercicos?""

palavras = texto.split()

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrências

print(res.most_common(5))

# Testando Counter com Tupla

tupla = (1,2,2,3,2,2,3,3,1,1,4,4,4,2,2,3,3,1,1,1,5,5)

res = Counter(tupla)
print(res)

# As três palavras mais frequentes
print(res.most_common(3))
"""
