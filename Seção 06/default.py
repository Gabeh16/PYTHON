"""
Modulo collections - Default Dict

dicionario = {'curso': 'programação em Python'}

print(dicionario)

print(dicionario['curso'])

Defaultdict -> Uso quando não tiver um valor definido
caso eu tente acessar uma chave que não existe, essa
chave é criada e o valor default será atribuido

OBS: Lambdas são funções sem nome que podem receber
parâmetros e retornar.
"""
from collections import defaultdict

dicionario = defaultdict(lambda:0)

print(dicionario)

print(dicionario['outro']) # Sem KeyError


