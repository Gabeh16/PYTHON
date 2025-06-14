"""
Faça um programa que determine e mostre os cinco
primeiros multiplos de 3 considerando número maiores
que 0
"""

for num in range(3,16,3):
    print(num)

contador: int = 0
indice: int = 1

while contador < 5:
    if indice % 3 == 0:
        print(f"O numero {indice} é multiplo de 3")
        contador = contador + 1
    indice = indice + 1