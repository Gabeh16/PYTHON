"""
Loop while

Forma geral

while expressão boleana:
    //execução do loop

O bloco do while será escrito enquanto a expressão
booleana for verdadeira

Expressão Booleana é toda expressão verdadeira ou
falsa

exemplo:

num = 5
num < 5
false

#Exemplo 1
numero = 1
while numero < 10:
    print(numero)
    numero = numero + 1

#OBS: em um loop while é preciso observar a parada

#Exemplo 2
resposta = 1

while resposta != 'sim':
    resposta = input("Já acabou? ")
"""
num = 1

while num < 11:
    print(num)
    num = num + 1