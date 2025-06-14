"""
Escopo  de Variáveis

Dois casos de escopo:
1 - Variáveis globais
 - Variáveis globais são reconhecidas, por todo
 o programa

2 - Variáveis Locais
 - Variáveis locais são limitadas ao local onde
 foi declarada
"""
numero = 42 #Variável global
print(numero)

numero = 42

if numero > 10:
    novo = numero + 10 #Variável local
    print(novo)