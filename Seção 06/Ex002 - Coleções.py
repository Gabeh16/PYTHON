"""
Faça um programa que possua uma lista denominada A que
armazene 6 números inteiros. O programa
deve executar os seguintes passos:
A) Atribua os seguintes valores a essa lista
1,0,5,-2,-5,7.
B) Armazene em uma variável inteira a soma entre os
valores das posições A[0], A[1], e A[5] e mostre na
tela a soma
C)

"""

a = [1,0,5,-2,-5,7]
print(a)

var1 = a[0] + a[1] + a[5]
print(var1)

a.insert(5,100)
print(a)

# Separa os valores da lista um em cada linha
for lista in a:
    print(lista)